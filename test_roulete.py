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


def roulette_choice1(w):
    # generate accumulate weight list.
    # It can be also made by using numpy.cumsum()
    tot = np.cumsum(np.reciprocal(w))

    r = random.random() * max(tot)
    # generate a random integer and search it in linear manner.
    # It can be also made by using bisect.bisect_right(tot, r)
    i = bisect.bisect_right(tot, r)
    return i

if __name__ == "__main__":
    w = np.arange(100,dtype = 'float') + 1
    np.random.shuffle(w)
    test = [0]*len(w)
    for x in range(100000):
        i = roulette_choice1(w)
        test[i] += 1
    print(sum(test))
    for j,s in enumerate(w):
        print("{0}: {1}回".format(s,test[j]))