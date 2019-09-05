import random
import sys
import re
import time
import copy
import numpy as np
import csv
import bisect
import matplotlib.pyplot as plt
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

def main():
    n = 20
    i = 0
    x = np.arange(n + 1)
    count = np.zeros(n + 1)
    while(i < 10000):
        set_l = 0
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

        rand = (1 / np.square(y))

        if(rand <= 20 and rand >= 1):
            i += 1
            count[int(rand)] += 1
    
    plt.plot(x ,count / 10000)
    s = r"C:\Users\imada\Desktop\Research\tsp\levy.png"
    plt.savefig(s)

if __name__ == '__main__':
    main()