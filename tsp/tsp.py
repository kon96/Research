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

class Individual(object):
    def __init__(self,size):
        self.root = np.arange(size)
        np.random.shuffle(self.root)
        self.cost = np.zeros(size,float)

    def calc_root(self,co):
        for i in range(len(self.root) - 1):
            self.cost[i] = np.linalg.norm(co[self.root[i + 1]] - co[self.root[i]] )

        self.cost[i + 1] = np.linalg.norm(co[self.root[0]] - co[self.root[i + 1]] )

        self.total_cost = sum(self.cost)

            
def roulette_choice1(w):
    tot = np.cumsum(np.reciprocal(w))

    r = random.random() * max(tot)
    
    i = bisect.bisect_right(tot, r)
    return i


def cross(pop,cl):
    offspring = copy.deepcopy(pop)
    p_c = 0.8
    a = np.arange(len(pop))
    np.random.shuffle(a)
    for k in range(0, int(len(pop) * p_c), 2):
        c1 = offspring[a[k]]
        c2 = offspring[a[k + 1]]
        while(1):
            r1 = random.randint(0,cl - 1)
            r2 = random.randint(0,cl - 1)
            if(r1 != r2):
                break

        e1 = copy.deepcopy(c1.root[r1:r2])
        e2 = copy.deepcopy(c2.root[r1:r2])
        child1 = np.arange()
        child2 = np.arange()

        for i in range(cl):
            if( c2[i] not in e1):
                child1 = np.append(child1,c2.root[i])
            if( c1[i] not in e2):
                child2 = np.append(child2,c1.root[i])

        child1 = np.insert(child1, r1, e1)
        child2 = np.insert(child2, r1, e2)

        offspring[a[k]].root = child1
        offspring[a[k + 1]].root = child2

    return offspring


def mutate(ind, cl):
    while(1):

        r1 = random.randint(0,cl - 1)
        r2 = random.randint(0,cl - 1)
        if(r1 != r2):
            break
    
    ind[r1],ind[r2] = ind[r2],ind[r1]

    return ind

def create_pop(num,size):
    pop = []
    for i in range(num):
        ind = Individual(size)
        pop.append(ind)
    
    return pop

def main():
    start = time.time()
    pop = create_pop()
    NGEN = 20000
    ind_num = 100
    m = 10
    c = 0
    tsp_data = open(r"C:\Users\imada\Desktop\Research\tsp\burma14.txt","r")

    lines = tsp_data.readlines()
    tsp_data.close()

    size = len(lines)

    co = np.empty((0,2), float)

    for i,line in enumerate(lines):
        x = float(line.split()[1])
        y = float(line.split()[2])
        co = np.append(co,np.array([[x,y]]), axis=0)   
        print("{0} {1}".format(co[i][0],co[i][1]))

    for g in range(NGEN):
        cross(pop,size)

    

if __name__ == '__main__':
    main()

