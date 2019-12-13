import random
import sys
import re
import time
import copy
import numpy as np
import csv
import bisect
sys.path.append('/usr/local/lib/python3.6/dist-packages')

from datetime import datetime
from joblib import Parallel,delayed
from simanneal import Annealer
from scoop import futures
from deap import base
from deap import creator
from deap import tools
from deap import cma
from itertools import zip_longest

set_l = 0
y1 = 0
y2 = 0

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

        count[i] += 1

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


def mutate(pop, size, m):
    for mutant in pop:
        r = random.random()
        if(r < m):
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

def levy(m,t):
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
        if(x <= 15 and x >= 1):
            return int(x)

def main():
    start = time.time()
    m = 0.2         #突然変異率
    p_c = 0.8       #交叉率
    NGEN = 20000    #世代数
    ind_num = 100   #集団の大きさ
    
    files = ["att532","berlin52","burma14","eil76","kroA100","lin105","lin318","pr76","pr439","pr1002","rat783","st70"]

    for tsp_f in files:

        input_f = r"C:\Users\imada\Desktop\Research\tsp\\" + tsp_f +".txt" 
        tsp_data = open(input_f,"r")
        lines = tsp_data.readlines()
        tsp_data.close()

        size = len(lines)    #個体の大きさ

        co = np.empty((0,2), float)

        for i,line in enumerate(lines):
            x = float(line.split()[1])
            y = float(line.split()[2])
            co = np.append(co,np.array([[x,y]]), axis=0)   
            print("{0} {1}".format(co[i][0],co[i][1]))

        dist = init_cost(co)
        
        pop = create_pop(ind_num,size)
        calc_fit(pop,dist)
        w = np.zeros(len(pop),float)

        for g in range(NGEN):
            print("-------第{0}世代-------".format(g))
            for i in range(len(pop)):
                w[i] = pop[i].total_cost
            pop = roulette_choice1(pop,w)
            print("Max:{0}\nMin:{1}\nave:{2}\nBest root:{3}".format(max(w),min(w),sum(w) / 100,pop[np.argmin(w)].root))
            for i in range(len(pop)):
                w[i] = pop[i].total_cost
            pop = cross(pop,size,p_c)
            pop = mutate(pop,size,m)
            calc_fit(pop,dist)

        print("-------第{0}世代-------".format(g + 1))
        for i in range(len(pop)):
            w[i] = pop[i].total_cost

        print("Max:{0}\nMin:{1}\nBest root:{2}".format(max(w),min(w),pop[np.argmin(w)].root))
        elapsed_time = (time.time() - start) / 3600 
        print("elapsed_time:{0}".format(elapsed_time) + "[h]")

if __name__ == '__main__':
    main()
