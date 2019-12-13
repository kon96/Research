import random
import sys
import re
import time
import copy
import numpy as np
import bisect
import matplotlib.pyplot as plt
sys.path.append('/usr/local/lib/python3.6/dist-packages')

from datetime import datetime
from joblib import Parallel,delayed
from itertools import zip_longest

set_l = 0
y1 = 0
y2 = 0

o_length = 0
sumInc = 0
alpha = 5
Bgn = [0] * alpha

class Individual(object):
    def __init__(self,size):
        self.root = np.arange(size)
        np.random.shuffle(self.root)
        self.change = True
        self.cost = np.zeros(size,float)

    def calc_root(self,dist):
        for i in range(len(self.root) - 1):
            self.cost[i] = dist[self.root[i]][self.root[i + 1]]

        self.cost[i + 1] = dist[self.root[i + 1]][self.root[0]]

        self.total_cost = np.sum(self.cost)

        self.change = False

def calc_fit(pop,dist):
    for i in pop:
        if(i.change):
            i.calc_root(dist)
    
    return pop

            
def roulette_choice1(pop,w):
    if(max(w) == min(w)):
        return pop
    new_pop = []
    tot = []
    tmp = np.zeros(len(pop),float)
    count = [0] * len(pop)

    for t,fit in enumerate(w):
        tmp[t] = (max(w) - fit) / (max(w) - min(w))

    elite = w.argsort()[0:5]
    for x in elite:
        new_pop.append(pop[x])
    
    tot = np.cumsum(tmp)

    for j in range(len(pop) - 5):
        r = random.random() * max(tot)
        i = bisect.bisect_right(tot, r)

        new_pop.append(copy.deepcopy(pop[i]))

    return new_pop


def cross(pop,size,p_c):
    offspring = copy.deepcopy(pop)
    cross_num = int(len(pop) * p_c) + 2
    a = np.arange(len(pop))
    np.random.shuffle(a)
    for k in range(0, cross_num, 2):
        c1 = offspring[a[k]]
        c2 = offspring[a[k + 1]]
        while(1):
            r1 = random.randint(0,size - 1)
            r2 = random.randint(0,size - 1)
            if(r1 != r2):
                if(r2 < r1):
                    r1, r2 = r2, r1
                break

        e1 = copy.deepcopy(c1.root[r1:r2])
        e2 = copy.deepcopy(c2.root[r1:r2])
        child1 = np.arange(0)
        child2 = np.arange(0)

        for i in range(size):
            if( c2.root[i] not in e1):
                child1 = np.append(child1,c2.root[i])
            if( c1.root[i] not in e2):
                child2 = np.append(child2,c1.root[i])

        child1 = np.insert(child1, r1, e1)
        child2 = np.insert(child2, r1, e2)

        offspring[a[k]].root = child1
        offspring[a[k + 1]].root = child2

        offspring[a[k]].change = True
        offspring[a[k + 1]].change = True

    return offspring


def mutate_l(pop, size, p_m,move):
    for mutant in pop:
        r = random.random()
        if(r < p_m):
            for i in range(levy(0,0.5,10)):
                while(1):
                    r1 = random.randint(0,size - 1)
                    walk = levy(0,0.5,move)
                    if(r % 2 == 0):
                        r2 = r1 + walk
                    else:
                        r2 = r1 - walk
                    
                    if(r2 >= 0 and r2 <= size):
                        break
                    
                mutant.root[r1],mutant.root[r2] = mutant.root[r2],mutant.root[r1]

    return pop

def mutate(pop,size,p_m):
    for mutant in pop:
        r = random.random()
        if(r < p_m):
            while(1):
                r1 = random.randint(0,size - 1)
                r2 = random.randint(0,size - 1)
                if(r1 != r2):
                    break

            mutant.root[r1],mutant.root[r2] = mutant.root[r2],mutant.root[r1]

    return pop

def create_pop(num,size):
    pop = []
    for i in range(num):
        ind = Individual(size)
        pop.append(ind)
    
    return pop

def init_cost(co):
    c = np.zeros((len(co),len(co)))
    for i in range(len(co)):
        for j in range(len(co)):
            c[i][j] = np.linalg.norm(co[j] - co[i])

    return c

def levy(m,t,move):
    global set_l,y1,y2
    while(1):
        if(set_l == 0):
            while(1):
                u1 = np.random.rand()
                u2 = np.random.rand()
                if(u1 != 0 and u2 != 0):
                    break
            r = np.sqrt(-2 * np.log(u1))
            t = (np.pi * u2) / 2

            y1 = r * np.cos(t)
            y2 = r * np.sin(t)

            set_l = 1
            y = y1
        elif(set_l == 1):
            y = y2
            set_l = 0

        x = m + (t / np.square(y))
        if(x <= move and x >= 1):
            return int(x)

def LK(ind,size,dist):
    global alpha
    global o_length
    global Bgn
    global sumInc
    i = 0
    restricted = np.zeros(size,dtype = int)
    copy_root = copy.deepcopy(np.insert(ind.root,len(ind.root),ind.root).tolist())
    l_root = ind.root.tolist()
    while(1):
        if(i >= size):
            break
        i += 1
        Bgn[0] = (Bgn[0] + 1) % size
        ind.calc_root(dist)
        o_length = ind.total_cost
        sumInc = 0
        if(i%100 == 0):
            print("i0 = {0}; i = {1}: {2},\r".format(Bgn[0],i,o_length))

        pathin = copy.deepcopy(copy_root[Bgn[0]:(Bgn[0]+size)])
        if(improvedPath(pathin, size, 1, restricted, l_root, dist)):
            i = 0
        ind.root = np.array(l_root)

def improvedPath(path, n, depth, restricted, pathout, dist):
    global alpha
    global o_length
    global Bgn
    global sumInc
    gmin = (o_length * (-1)) / n / 4 if n >= 10000 else (o_length * (-1)) / n / 2 
    if(depth < alpha):
        for j in range(n):
            i = (j + Bgn[depth]) % (n-1)
            nid = path[i]
            if(not restricted[nid]):
                g = dist[path[i]][path[i+1]] - dist[path[n-1]][path[i]]
                if(g > gmin):
                    sumInc += dist[path[i+1]][path[0]] - dist[path[n-1]][path[0]] - g 
                    path = Reverse(path,i+1,n-1)
                    if(sumInc < 0):
                        pathout[:] = path[:]
                        print("{0}#{1},\t\t\t \r".format(depth,(o_length + sumInc)))
                        return 1
                    restricted[nid] = 1
                    fimp = improvedPath(path, n, depth+1, restricted, pathout, dist)
                    restricted[nid] = 0
                    if(fimp):
                        return 1
            Bgn[depth] = (Bgn[depth] + 1) % (n-1)
    else:
        i = 0
        g = -2147483648
        for j in range(n-1):
            h = dist[path[j]][path[j+1]] - dist[path[n-1]][path[j]]
            if(h > g):
                g = h
                i = j
        if(g > 0):
            nid = path[i]
            sumInc += dist[path[i+1]][path[0]] - dist[path[n-1]][path[0]] - g
            path = Reverse(path,i+1,n-1)
            if(sumInc < 0):
                pathout[:] = path[:]
                print("{0}${1},\r".format(depth,o_length + sumInc))
                return 1
            restricted[nid] = 1
            fimp = improvedPath(path, n, depth+1, restricted, pathout, dist)
            restricted[nid] = 0
            if(fimp):
                return 1
    return 0

def Reverse(path, b, e):
    while(b < e):
        tmp = path[b]
        path[b] = path[e]
        path[e] = tmp
        b += 1
        e -= 1
    return path

def main():
    start = time.time()
    start_p_m = 0.4       #突然変異率
    p_c = 0.8       #交叉率
    NGEN = 100000    #世代数
    ind_num = 100   #集団の大きさ
    
    m_f = True #False ⇒ levy  True ⇒ GA

    tsp_f = "st70"

    input_f = r"C:\Users\imada\Desktop\Research\tsp\\" + tsp_f +".txt" 
    tsp_data = open(input_f,"r")
    lines = tsp_data.readlines()
    tsp_data.close()

    size = len(lines)    #個体の大きさ

    co = np.empty((0,2), float)
    plot_data = np.zeros(NGEN + 1,float)
    plot_x = np.arange(NGEN + 1)

    for i,line in enumerate(lines):
        x = float(line.split()[1])
        y = float(line.split()[2])
        co = np.append(co,np.array([[x,y]]), axis=0)   
        print("{0} {1}".format(co[i][0],co[i][1]))

    dist = init_cost(co)
        
    pop = create_pop(ind_num,size)
    calc_fit(pop,dist)
    w = np.zeros(len(pop),float)
    for i in range(len(pop)):
            w[i] = pop[i].total_cost
    
    p_m = start_p_m       #突然変異率
    p_ml = 0.4 
    move = (size * 0.3)       #移動範囲
    e_count = 0
    c_score = min(w)
    prev_score = min(w)
    start_score = min(w)

    LK(pop[0],size,dist)

if __name__ == '__main__':
    main()
