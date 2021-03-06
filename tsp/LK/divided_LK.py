import random
import sys
import re
import time
import copy
import numpy as np
import bisect
import matplotlib.pyplot as plt
import cython
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
        self.total_cost = 0

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

def calc_root(root,dist):
    total_cost = 0
    for i in range(len(root)-1):
        total_cost += dist[root[i]][root[i+1]]
    total_cost += dist[root[i+1]][root[0]]

    return int(total_cost)

def calc_half(root,dist,s_node,e_node):
    total_cost = 0
    total_cost += dist[s_node][root[0]]
    for i in range(len(root)-1):
        total_cost += dist[root[i]][root[i+1]]
    total_cost += dist[root[i+1]][e_node]

    return int(total_cost)

def calc_divided_root(root,dist,half_root):
    total_cost = 0
    for i in range(len(root)-1):
        total_cost += dist[root[i]][root[i+1]]
    total_cost += dist[root[i+1]][root[0]] #+ half_root

    return int(total_cost)

"""def calc_divided_root(root,dist,s_node,e_node,half_root):
    total_cost = 0
    for i in range(len(root)-1):
        if(root[i+1] < (len(root) - 1) or root[i] < (len(root) - 1)):
            total_cost += dist[root[i]][root[i+1]]     
        elif(root[i+1] == len(root)-1):
            total_cost += dist[root[i]][s_node] + half_root
        elif(root[i] == len(root) - 1):
            total_cost += dist[e_node][root[i+1]]

    if(root[i+1] == len(root) - 1):
        total_cost += dist[e_node][root[0]]
    else:
        total_cost += dist[i+1][root[0]]

    return int(total_cost)
    """

def calc_ind(ind,dist):
    for i in range(len(ind.root) - 1):
        ind.cost[i] = dist[ind.root[i]][ind.root[i + 1]]

    ind.cost[i + 1] = dist[ind.root[i + 1]][ind.root[0]]
    ind.total_cost = int(np.sum(ind.cost))
    ind.change = False

def calc_pop(pop,dist,w):
    for i,ind in enumerate(pop):
        if(ind.change):
            calc_ind(ind,dist)
            w[i] = ind.total_cost

def roulette_choice1(pop,w):
    if(max(w) == min(w)):
        return pop
    new_pop = []
    tot = []
    tmp = np.zeros(len(pop),float)

    for t,fit in enumerate(w):
        tmp[t] = (max(w) - fit) / (max(w) - min(w))

    #elite = w.argsort()[0:5]
    elite = [np.argmin(w)] * 5
    for x in elite:
        new_pop.append(copy.deepcopy(pop[x]))
    
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

def LK(ind,size,dist):
    global alpha
    global o_length
    global Bgn
    global sumInc
    i = 0
    restricted = np.zeros(size,dtype = int)   
    l_root = ind.root.tolist()
    while(1):
        if(i >= size):
            break
        i += 1
        Bgn[0] = (Bgn[0] + 1) % size
        calc_ind(ind,dist)
        o_length = ind.total_cost
        sumInc = 0
        if(i%100 == 0):
            print("i0 = {0}; i = {1}: {2},\r".format(Bgn[0],i,o_length))

        copy_root = copy.deepcopy(np.insert(ind.root,len(ind.root),ind.root).tolist())
        pathin = copy.deepcopy(copy_root[Bgn[0]:(Bgn[0]+size)])

        if(improvedPath(pathin, size, 1, restricted, l_root, dist)):
            i = 0
        ind.root = np.array(l_root)

def divided_LK(root,o_size,dist,half,co):
    global alpha
    global o_length
    global Bgn
    global sumInc
    for l in range(2):
        roop_count = 0
        if(half):
            divided_root = root[0:int(o_size/2)]
            s_node = root[int(o_size/2)]
            e_node = root[len(root)-1]
            half_root = calc_half(root[int(o_size/2):len(root)],dist,s_node,e_node)
        elif(not half):
            divided_root = root[int(o_size/2):len(root)]
            s_node = root[0]
            e_node = root[int(o_size/2)-1]
            half_root = calc_root(root[0:int(o_size/2)],dist)
        
        divided_root = np.insert(divided_root,len(divided_root),o_size)
        size = len(divided_root)

        s_node = e_node

        tmp1 = np.zeros(o_size)
        tmp2 = np.zeros(o_size)
        for x in range(o_size):
            tmp1[x] = np.linalg.norm(co[s_node] - co[x])
            tmp2[x] = np.linalg.norm(co[x] - co[e_node])
        tmp2 = np.append(tmp2,0)
        div_dist = np.append(dist,tmp1.reshape((len(tmp1),1)),axis = 1)
        div_dist = np.append(div_dist,tmp2.reshape(1,len(tmp2)),axis = 0)

        i = 0
        restricted = np.zeros(o_size + 1,dtype = int)  
        l_root = divided_root.tolist()
        while(1):
            if(i >= size):
                break
            i += 1
            Bgn[0] = (Bgn[0] + 1) % (size)
            
            o_length = calc_divided_root(divided_root,div_dist,half_root)
            sumInc = 0
            if(i%100 == 0):
                print("i0 = {0}; i = {1}: {2}".format(Bgn[0],i,o_length))

            copy_root = copy.deepcopy(np.insert(divided_root,size,divided_root).tolist())
            pathin = copy.deepcopy(copy_root[Bgn[0]:(Bgn[0]+size)])

            if(improvedPath(pathin, size, 1, restricted, l_root, div_dist)):
                i = 0
                roop_count += 1
                if(roop_count == 10000):
                    divided_root = np.array(l_root)
                    break

            divided_root = np.array(l_root)

        if(half):
            root = copy.deepcopy(np.insert(divided_root,np.argmax(divided_root),root[int(o_size/2):o_size]))
            root = np.delete(root,np.argmax(root))
        elif(not half):
            root = copy.deepcopy(np.insert(divided_root,np.argmax(divided_root),root[0:int(o_size/2)]))
            root = np.delete(root,np.argmax(root))
        half = not half
        print("end")

    return root

def improvedPath(path, n, depth, restricted, pathout, dist):
    global alpha
    global o_length
    global Bgn
    global sumInc
    gmin = int((o_length * (-1)) / n / 4 if n >= 10000 else (o_length * (-1)) / n / 2 )
    if(depth < alpha):
        for j in range(n):
            i = (j + Bgn[depth]) % (n-1)
            nid = path[i]
            #ここ以下を修正
            if(not restricted[nid]):
                g = int(dist[path[i]][path[i+1]] - dist[path[n-1]][path[i]])
                if(g > gmin):
                    #sumInc += int(dist[path[i+1]][path[0]] - dist[path[n-1]][path[0]] - g )
                    path = Reverse(path,i+1,n-1)
                    path_length = calc_root(path,dist)
                    if(path_length < o_length):
                        pathout[:] = path[:]
                        print("\r{0}#{1}\t\t\t".format(depth,(o_length + sumInc)),end="")
                        return 1
                    """sumInc = int(sumInc)
                    if(sumInc < 0):
                        pathout[:] = path[:]
                        print("\r{0}#{1}\t\t\t".format(depth,(o_length + sumInc)),end="")
                        return 1"""
                    restricted[nid] = 1
                    fimp = improvedPath(path, n, depth+1, restricted, pathout, dist)
                    path_length = calc_root(path,dist)
                    restricted[nid] = 0
                    if(fimp and path_length < o_length ):
                        return 1
            Bgn[depth] = (Bgn[depth] + 1) % (n-1)
    else:
        i = 0
        g = -2147483648
        for j in range(n-1):
            h = int(dist[path[j]][path[j+1]] - dist[path[n-1]][path[j]])
            if(h > g):
                g = h
                i = j
        if(g > 0):
            nid = path[i]
            #sumInc += int(dist[path[i+1]][path[0]] - dist[path[n-1]][path[0]] - g)
            path = Reverse(path,i+1,n-1)
            #sumInc = int(sumInc)
            if(calc_root(path,dist) < o_length):
                        pathout[:] = path[:]
                        print("\r{0}#{1}\t\t\t".format(depth,(o_length + sumInc)),end="")
                        return 1
            """if(sumInc < 0):
                pathout[:] = path[:]
                print("\r{0}${1}\t\t\t".format(depth,o_length + sumInc),end = "")
                return 1"""
            restricted[nid] = 1
            fimp = improvedPath(path, n, depth+1, restricted, pathout, dist)
            restricted[nid] = 0
            if(fimp and calc_root(path,dist) < o_length):
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
    start_p_m = 0.35       #突然変異率
    p_c = 0.8       #交叉率
    NGEN = 20000    #世代数
    ind_num = 60   #集団の大きさ

    
    m_f = not False #False ⇒ levy  True ⇒ GA
    half = True #False ⇒ 後半  True ⇒ 前半 

    tsp_f = "att532"

    input_f = r"C:\Users\imada\Desktop\Research\tsp\\" + tsp_f +".txt" 
    tsp_data = open(input_f,"r")
    lines = tsp_data.readlines()
    tsp_data.close()

    size = len(lines)    #個体の大きさ

    co = np.empty((0,2), float)
    tour_x = np.empty(0,float)
    tour_y = np.empty(0,float)
    plot_data = np.zeros(NGEN + 1,float)
    plot_x = np.arange(NGEN + 1)

    for i,line in enumerate(lines):
        x = float(line.split()[1])
        y = float(line.split()[2])
        co = np.append(co,np.array([[x,y]]), axis=0) 
        print("{0} {1}".format(co[i][0],co[i][1]))

    dist = init_cost(co)
        
    pop = create_pop(ind_num,size)
    w = np.zeros(len(pop),int)
    calc_pop(pop,dist,w)
    
    p_m = start_p_m       #突然変異率
    p_ml = start_p_m 
    move = (size * 0.3)       #移動範囲
    e_count = 0
    mutate_count = 0
    c_score = min(w)
    prev_score = min(w)
    m = np.argmin(w)

    for g in range(NGEN):
        g_start = time.time()

        #if(g == 60000):
            #m_f = not m_f
        if(g % 20000 == 0):
            p_m -= 0.05
            p_ml -= 0.05
            #if(g <= 60000):
             #   p_m -= 0.05
            #else:
             #   p_ml -= 0.05
        
            
        print("-------第{0}世代-------".format(g))

        print("Max:{0}\nMin:{1}\nave:{2}\nBest Score:{3}\nBest root:{4}\ne_count:{5}".format(max(w),min(w),(sum(w) / ind_num),prev_score,pop[np.argmin(w)].root,e_count))
        plot_data[g] = min(w)
        c_score = min(w)

        pop = roulette_choice1(pop,w)
        pop = cross(pop,size,p_c)
        if(m_f):
            pop = mutate(pop,size,p_m)
            mutate_count += 1
            if(mutate_count == 200):
                m_f = not m_f
                mutate_count = 0
        elif(not m_f):
            pop = mutate_l(pop,size,p_ml,move)
        
        calc_pop(pop,dist,w)

        if(prev_score <= c_score):
            e_count += 1
            if(e_count % 100 == 0):
                """if(e_count == 100):
                    m = np.argmin(w)
                else:
                    m = np.random.randint(0,len(pop))"""
                m = np.argmin(w)
                pop[m].root = divided_LK(pop[m].root,size,dist,half,co)
                half = not half
                calc_ind(pop[m],dist)    
                w[m] = pop[m].total_cost
                c_score = w[m]
                print()
                if(prev_score > c_score):
                    prev_score = c_score
                    best_root = pop[m].root
                    e_count = 0
                elif(e_count % 50 == 0):
                    m_f = not m_f           
        else:
            prev_score = c_score
            best_root = pop[m].root
            e_count = 0

        
        g_end = time.time()
        print("m_f:{0}".format(m_f))
        print("remaining time{0}".format((g_end - g_start) * (NGEN - g) / 3600))

    print("-------第{0}世代-------".format(g + 1))

    calc_pop(pop,dist,w)

    print("Max:{0}\nMin:{1}\nBest root:{2}".format(max(w),min(w),pop[np.argmin(w)].root))
    plot_data[g + 1] = min(w)
    min_2 = str(prev_score)
    plt.plot(plot_x,plot_data)
        
    title = min_2
    plt.title(title)
    
    output_f = r"C:\Users\imada\Desktop\Research\tsp\LK\\divided_output\\" + tsp_f + "d_{0}_{1}_{2}_{3}_{4}_{5}.png".format(NGEN,p_c,start_p_m,ind_num,move,m_f)
    plt.savefig(output_f)
    elapsed_time = (time.time() - start) / 3600 
    print("elapsed_time:{0}".format(elapsed_time) + "[h]")

    plt.show()
    plt.cla()

    for s in range (len(best_root)):
        tour_x = np.append(tour_x,co[best_root[s]][0])
        tour_y = np.append(tour_y,co[best_root[s]][1])
        txt = "{0}:".format(s) + str(best_root[s])    
        #plt.annotate(txt,xy=(co[best_root[s]][0],co[best_root[s]][1]))
    tour_x = np.append(tour_x,co[best_root[0]][0])
    tour_y = np.append(tour_y,co[best_root[0]][1])
    last_x = [tour_x[size-1],tour_x[0]]
    last_y = [tour_y[size-1],tour_y[0]]
    plt.plot(tour_x[0:int(size/2)],tour_y[0:int(size/2)],marker = '.',color='c',markersize=10)
    plt.plot(tour_x[int(size/2)-1:int(size/2)+1],tour_y[int(size/2)-1:int(size/2)+1],color='c',markersize=10)
    plt.plot(tour_x[int(size/2):size],tour_y[int(size/2):size],marker = '.',color='k',markersize=10)
    plt.plot(last_x,last_y,color='k',markersize=10)
    plt.plot(co[best_root[0]][0],co[best_root[0]][1],marker = '.',color='r',markersize=10)
    ticks = np.arange(0,0.001,10000)
    plt.yticks(ticks)
    plt.xticks(ticks)
    plt.show()



if __name__ == '__main__':
    main()
