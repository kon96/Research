import random
import sys
import re
import time
import copy
import numpy as np
import csv
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

d_e_n_pattern1 = np.array([0,6,7,8,9,10,12,19,20,21,22,23])
d_e_n_pattern2 = np.array([1,2,3,4,5,13,14,15,16,17,24])

#ALL
all_employees = np.array([i for i in range(0,25)])
max_num_d = np.array([11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,18,11,11,11,11,11,11,11])
min_num_d = np.array([8,8,8,8,7,8,8,8,7,7,7,7,7,8,8,8,8,8,7,8,8,8,13,8,8,7,8,8,8,8])
max_num_e = np.array([4 for i in range(30)])
min_num_e = np.array([4 for i in range(30)])
max_num_n = np.array([3 for i in range(30)])
min_num_n = np.array([3 for i in range(30)])
max_num_f = np.array([(25 - (min_num_d[i] + 7)) for i in range(30)])
min_num_f = np.array([(25 - (max_num_d[i] + 7)) for i in range(30)])

#1-9 = 1,9
g_1_9 = np.array([0,8])
max_num_1_9_d = np.array([2 for i in range(30)])
min_num_1_9_d = np.array([0 for i in range(30)])
max_num_1_9_e = np.array([1 for i in range(30)])
min_num_1_9_e = np.array([0 for i in range(30)])
max_num_1_9_n = np.array([1 for i in range(30)])
min_num_1_9_n = np.array([0 for i in range(30)])

#A_SS = 1,2,3,4,5,6
g_A_SS = np.array([0,1,2,3,4,5])
max_num_A_SS_d = np.array([2,3,3,3,2,3,2,3,2,2,2,2,2,2,3,2,2,3,2,2,3,3,6,2,2,2,3,3,3,2])
min_num_A_SS_d = np.array([2 for i in range(30)])
max_num_A_SS_e = np.array([1 for i in range(30)])
min_num_A_SS_e = np.array([1 for i in range(30)])
max_num_A_SS_n = np.array([1 for i in range(30)])
min_num_A_SS_n = np.array([1 for i in range(30)])

#B_rq_s = 19,20,21,22,23,24,25
g_B_rq_s = np.array([18,19,20,21,22,23,24])
max_num_B_rq_s_d = np.array([4,6,6,6,4,6,4,6,4,4,4,4,4,4,6,4,4,6,4,4,5,6,6,4,4,4,6,6,6,4])
min_num_B_rq_s_d = np.array([2 for i in range(30)])
max_num_B_rq_s_e = np.array([1 for i in range(30)])
min_num_B_rq_s_e = np.array([1 for i in range(30)])
max_num_B_rq_s_n = np.array([2 for i in range(30)])
min_num_B_rq_s_n = np.array([0 for i in range(30)])

#B_SS = 14,15,16,17,18
g_B_SS = np.array([13,14,15,16,17])
max_num_B_SS_d = np.array([2,3,3,3,2,3,2,3,1,1,1,2,1,2,3,2,2,3,2,1,3,3,6,2,2,2,3,3,3,2])
min_num_B_SS_d = np.array([1,1,1,1,1,1,1,1,0,0,0,1,0,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1])
max_num_B_SS_e = np.array([1 for i in range(30)])
min_num_B_SS_e = np.array([1 for i in range(30)])
max_num_B_SS_n = np.array([1 for i in range(30)])
min_num_B_SS_n = np.array([0 for i in range(30)])

#B_SS_s = 14,15,16,17,18,25
g_B_SS_s = np.array([13,14,15,16,17,24])
max_num_B_SS_s_d = np.array([3,3,3,3,2,3,3,3,2,2,2,2,2,3,3,3,3,3,2,2,3,3,6,3,3,2,3,3,3,3])
min_num_B_SS_s_d = np.array([2,2,2,2,2,2,2,2,1,1,1,2,1,2,2,2,2,2,2,1,2,2,2,2,2,2,2,2,2,2])
max_num_B_SS_s_e = np.array([2 for i in range(30)])
min_num_B_SS_s_e = np.array([1 for i in range(30)])
max_num_B_SS_s_n = np.array([1 for i in range(30)])
min_num_B_SS_s_n = np.array([1 for i in range(30)])

#GroupA = 1,2,3,4,5,6,7,8,9,10,11,12,13
g_A = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12])
max_num_A_d = np.array([6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,9,6,6,6,6,6,6,6])
min_num_A_d = np.array([4,4,4,4,3,4,4,4,4,4,4,3,4,4,4,4,4,4,3,4,4,4,6,4,4,3,4,4,4,4])
max_num_A_e = np.array([2 for i in range(30)])
min_num_A_e = np.array([2 for i in range(30)])
max_num_A_n = np.array([2 for i in range(30)])
min_num_A_n = np.array([1 for i in range(30)])

#GroupB = 14,15,16,17,18,19,20,21,22,23,24,25
g_B = np.array([13,14,15,16,17,18,19,20,21,22,23,24])
max_num_B_d = np.array([6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,9,6,6,6,6,6,6,6])
min_num_B_d = np.array([4,4,4,4,3,4,4,4,4,4,4,3,4,4,4,4,4,4,3,4,4,4,6,4,4,3,4,4,4,4])
max_num_B_e = np.array([2 for i in range(30)])
min_num_B_e = np.array([2 for i in range(30)])
max_num_B_n = np.array([2 for i in range(30)])
min_num_B_n = np.array([1 for i in range(30)])

#勤務希望
request = np.array([ 
    [],
    [1,8,17],
    [1],
    [10,11,24,25],
    [21,22,23,24],
    [15,16],
    [0],
    [24,25],
    [0,11,22],
    [],
    [8],
    [6,7,8],
    [8,9,10,24,25,26],
    [10,11,12,26],
    [17],
    [19],
    [19,20],
    [0,9,10],
    [22,23,24,25],
    [8,17,18],
    [7],
    [8],
    [8,9],
    [1,2,24,25],
    []
])

#その他の勤務
other = np.array([
    [],[12],[],[19],[],[],[],[9],[],[0,15],[15],[15],[6],[9],[],[12,20],[12],[19],[6,15],[29],[29],[0,29],[29],[],[]
])

#禁止勤務パターン
b_shift = ['[0|5][1-4][0|5]','[1-4]{7}','[0|5]{6}','[1][^1]{7}',
           '[^3][3][^3]','[3][0-5]{2}[3]','[3][0-5]{3}[3]',
           '[3][0-5]{4}[3]','[3][0-5]{5}[3]','[3]{3}',
           '[1]{5}','[2]{4}','[3][1]','[3][2]','[3][4]','[2][1]',
           '[2][4]','[3][0|5][1]'
]


class Nurse(object):

    def __init__(self,no,request,other):
        self.no = no
        self.request = request
        self.other = other
        self.shift = []
        for i in range(30):
            self.shift.append(random.randint(0,3))

    def req_init(self):
        if(len(self.request) != 0):
            for i in self.request:
                self.shift[i] = 5

        if(len(self.other) != 0):
            for j in self.other:
                self.shift[j] = 4
    
    def check(self):
        penalty = 0
        d = self.shift.count(1)
        e = self.shift.count(2)
        n = self.shift.count(3)
        f = self.shift.count(0) + self.shift.count(5)

        if(d > 15):
            penalty += 1
        if(e > 6 or e < 4):
            penalty += 1
        if(n > 4 or n < 2):
            penalty += 1
        if(f < 9):
            penalty += 1
        for i in self.other:
            if(self.shift[i] != 4):
                penalty += 5
        

        map_l = map(str,self.shift)
        pattern = ''.join(map_l)
        for x in b_shift:
            y = re.findall(x,pattern)
            penalty += len(y)
        
        return penalty

class Shift_G(object):
    
    def __init__(self,d_max,d_min,e_max,e_min,n_max,n_min,group):
        self.d_max = d_max
        self.d_min = d_min
        self.e_max = e_max
        self.e_min = e_min
        self.n_max = n_max
        self.n_min = n_min
        self.d = 0
        self.e = 0
        self.n = 0
        self.f = 0
        self.group = group
        self.shift = np.empty((len(group),30),int)
    
    def check(self,pop):
        penalty = 0
        for i,g in enumerate(self.group):
            self.shift[i][:] = pop[g][:]
            
        self.d = np.sum(self.shift == 1, axis = 0)
        self.e = np.sum(self.shift == 2, axis = 0)
        self.n = np.sum(self.shift == 3, axis = 0)

        p1 = np.sum((self.d_max < self.d) | (self.d_min > self.d))
        p2 = np.sum((self.e_max < self.e) | (self.e_min > self.e))
        p3 = np.sum((self.n_max < self.n) | (self.n_min > self.n))

        penalty =  p1 + p2 + p3
        return penalty 

    def error(self,pop):
        enum = 0

        for i,g in enumerate(self.group):
            self.shift[i][:] = pop[g][:]
            
        self.d = np.sum(self.shift == 1, axis = 0)
        self.e = np.sum(self.shift == 2, axis = 0)
        self.n = np.sum(self.shift == 3, axis = 0)

        enum += np.sum((self.d_max < self.d) | (self.d_min > self.d))
        enum += np.sum((self.e_max < self.e) | (self.e_min > self.e))
        enum += np.sum((self.n_max < self.n) | (self.n_min > self.n))

        return enum

    """def save(self,writer):
        writer.writerow(self.d_max)
        writer.writerow(self.d_min)
        writer.writerow(self.e_max)
        writer.writerow(self.e_min)
        writer.writerow(self.n_max)
        writer.writerow(self.n_min)
        writer.writerow("\n")"""

"""class LocalSearch(Annealer):

    def __init__(self, init_state):
        super(LocalSearch,self).__init__(init_state)

    def move(self):
        n1 = random.choice(list(range(len(self.state))))
        while(1):
            s = random.choice(list(range(len(self.state[n1]) - 1 )))
            c = s + 1
            if(self.state[n1][c] <= 3 and self.state[n1][s] <= 3 and self.state[n1][s] != self.state[n1][c]):
                if(self.state[n1][c] > 1 or self.state[n1][s] > 1):
                    ind2 = self.state[:,s]
                    x = np.where(ind2 == self.state[n1][c])
                    n2 = None

                    for i in range(len(x[0])):
                        if(self.state[x[0][i]][c] == self.state[n1][s]):
                            n2 = x[0][i]
                            break

                    if(n2 != None):
                        self.state[n2][s],self.state[n2][c] = self.state[n2][c],self.state[n2][s]
            break
    
        self.state[n1][s],self.state[n1][c] = self.state[n1][c],self.state[n1][s]

    def energy(self):
       e = cal_p(self.state)
       return e"""

class LocalSearch(Annealer):

    def __init__(self, init_state):
        super(LocalSearch,self).__init__(init_state)

    def move(self):
        while(1):
            n1 = random.randint(0,23)
            n2 = n1 + 1
            j = random.choice(list(range(len(self.state[n1]))))
            if(self.state[n1][j] <= 3 and self.state[n2][j] <= 3):
                break
        self.state[n1][j],self.state[n2][j] = self.state[n2][j],self.state[n1][j]

    def energy(self):
       e = cal_p(self.state)
       return e

all_shift = Shift_G(max_num_d,min_num_d,max_num_e,min_num_e,max_num_n,min_num_n,all_employees)
o_n = Shift_G(max_num_1_9_d,min_num_1_9_d,max_num_1_9_e,min_num_1_9_e,max_num_1_9_n,min_num_1_9_e,g_1_9)
A = Shift_G(max_num_A_d,min_num_A_d,max_num_A_e,min_num_A_e,max_num_A_n,min_num_A_n,g_A)
A_SS = Shift_G(max_num_A_SS_d,min_num_A_SS_d,max_num_A_SS_e,min_num_A_SS_e,max_num_A_SS_n,min_num_A_SS_e,g_A_SS)
B = Shift_G(max_num_B_d,min_num_B_d,max_num_B_e,min_num_B_e,max_num_B_n,min_num_B_n,g_B)
B_SS = Shift_G(max_num_B_SS_d,min_num_B_SS_d,max_num_B_SS_e,min_num_B_SS_e,max_num_B_SS_n,min_num_B_SS_n,g_B_SS)
B_SS_s = Shift_G(max_num_B_SS_s_d,min_num_B_SS_s_d,max_num_B_SS_s_e,min_num_B_SS_s_e,max_num_B_SS_s_n,min_num_B_SS_s_n,g_B_SS_s)
B_rq_s = Shift_G(max_num_B_rq_s_d,min_num_B_rq_s_d,max_num_B_rq_s_e,min_num_B_rq_s_e,max_num_B_rq_s_n,min_num_B_rq_s_n,g_B_rq_s)

creator.create("FitnessShift", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness = creator.FitnessShift)

def Shift_init(pop):
    global max_num_f
    global min_num_f
    day = []
    for n,r in enumerate(request):
        if(len(r) != 0):
            for i in r:
                pop[n][i] = 5
    for n,o in enumerate(other):
        if(len(other) != 0):
            for j in o:
                pop[n][j] = 4
    d = np.sum(pop == 1, axis = 0)
    e = np.sum(pop == 2, axis = 0)
    n = np.sum(pop == 3, axis = 0)
    f = np.sum(pop == 0, axis = 0)
    f += np.sum(pop == 5, axis = 0)
    o = np.sum(pop == 4, axis = 0)
    max_num_f -= o
    min_num_f -= o 
    for i in range(30):
        day = pop[:,i]
        while(1):
            miss = 0
            if(d[i] > max_num_d[i]):
                miss += 1
                if(e[i] < min_num_e[i]):
                    day[np.where(day == 1)[0][np.random.randint(0,len(np.where(day == 1)[0]))]] = 2
                    d[i] -= 1
                    e[i] += 1
                elif(n[i] < min_num_n[i]):
                    day[np.where(day == 1)[0][np.random.randint(0,len(np.where(day == 1)[0]))]] = 3
                    d[i] -= 1
                    n[i] += 1
                elif(f[i] < min_num_f[i]):
                    day[np.where(day == 1)[0][np.random.randint(0,len(np.where(day == 1)[0]))]] = 0
                    d[i] -= 1
                    f[i] += 1
            elif (d[i] < min_num_d[i]):
                miss += 1
                if(e[i] > max_num_e[i]):
                    day[np.where(day == 2)[0][np.random.randint(0,len(np.where(day == 2)[0]))]] = 1
                    d[i] += 1
                    e[i] -= 1
                elif(n[i] > max_num_n[i]):
                    day[np.where(day == 3)[0][np.random.randint(0,len(np.where(day == 3)[0]))]] = 1
                    d[i] += 1
                    n[i] -= 1
                elif(f[i] > min_num_f[i]):
                    day[np.where(day == 0)[0][np.random.randint(0,len(np.where(day == 0)[0]))]] = 1
                    d[i] += 1
                    f[i] -= 1
            
            if(f[i] > max_num_f[i]):
                miss += 1
                if(e[i] < min_num_e[i]):
                    day[np.where(day == 0)[0][np.random.randint(0,len(np.where(day == 0)[0]))]] = 2
                    f[i] -= 1
                    e[i] += 1
                elif(n[i] < min_num_n[i]):
                    day[np.where(day == 0)[0][np.random.randint(0,len(np.where(day == 0)[0]))]] = 3
                    f[i] -= 1
                    n[i] += 1
                elif(d[i] < min_num_d[i]):
                    day[np.where(day == 0)[0][np.random.randint(0,len(np.where(day == 0)[0]))]] = 1
                    f[i] -= 1
                    d[i] += 1
            elif(f[i] < min_num_f[i]):
                miss += 1
                if(e[i] > max_num_e[i]):
                    day[np.where(day == 2)[0][np.random.randint(0,len(np.where(day == 2)[0]))]] = 0
                    f[i] += 1
                    e[i] -= 1
                elif(n[i] > max_num_n[i]):
                    day[np.where(day == 3)[0][np.random.randint(0,len(np.where(day == 3)[0]))]] = 0
                    f[i] += 1
                    n[i] -= 1
                elif(d[i] > min_num_d[i]):
                    day[np.where(day == 1)[0][np.random.randint(0,len(np.where(day == 1)[0]))]] = 0
                    f[i] += 1
                    d[i] -= 1
            
            if(e[i] > max_num_e[i]):
                miss += 1
                day[np.where(day == 2)[0][np.random.randint(0,len(np.where(day == 2)[0]))]] = 3
                e[i] -= 1
                n[i] += 1
            elif(e[i] < min_num_e[i]):
                miss += 1
                day[np.where(day == 3)[0][np.random.randint(0,len(np.where(day == 3)[0]))]] = 2
                e[i] += 1
                n[i] -= 1
            
            if(n[i] > max_num_n[i]):
                miss += 1
                day[np.where(day == 3)[0][np.random.randint(0,len(np.where(day == 3)[0]))]] = 0
                n[i] -= 1
                f[i] += 1
            elif(n[i] < min_num_n[i]):
                miss += 1
                day[np.where(day == 0)[0][np.random.randint(0,len(np.where(day == 0)[0]))]] = 3
                n[i] += 1
                f[i] -= 1
        
            if(miss == 0):
                break
        
        pop[:,i] = day[:]

    return pop

def employee_num(pop):
    p2 = 0
    p2 += all_shift.check(pop)
    p2 += A.check(pop)
    p2 += A_SS.check(pop)
    p2 += B.check(pop)
    p2 += B_SS.check(pop)
    p2 += B_SS_s.check(pop)
    p2 += B_rq_s.check(pop)
    p2 += o_n.check(pop)

    return p2

def ShiftPattern(pop):
    penalty = 0
    for i,ind in enumerate(pop):
        
        d = np.sum(ind == 1)
        e = np.sum(ind == 2)
        n = np.sum(ind == 3)
        f = np.sum(ind == 0)
        f += np.sum(ind == 5)

        if(i in d_e_n_pattern1):
            if(d > 15):
                penalty += 1
            if(e > 6 or e < 4):
                penalty += 1
            if(n > 4 or n < 2):
                penalty += 1
        elif(i in d_e_n_pattern2):
            if(d > 14):
                penalty += 1
            if(e > 6 or e < 4):
                penalty += 1
            if(n > 6 or n < 3):
                penalty += 1
        elif(i == 12):
            if(d > 17):
                penalty += 1
            if(e != 2):
                penalty += 1
            if(n != 2):
                penalty += 1
        elif(i == 18):
            if(d > 17):
                penalty += 1
            if(e > 4 or e < 2):
                penalty += 1
            if(n > 4):
                penalty += 1
        else:
            pass

        if(f < 9):
            penalty += 1

        map_l = map(str,ind)
        pattern = ''.join(map_l)
        for x in b_shift:
            y = re.findall(x,pattern)
            penalty += len(y)
    
    return penalty

def cxTwoPoint(pop):
    size = 29
    excluded = []
    t_list = []
    point_set = []
    ind_list = []
    for i in range(150):
        copy1 = copy.deepcopy(pop)
        copy2 = copy.deepcopy(pop)
        while(1):
            ind1 = random.randint(0,24)
            ind2 = random.randint(0,23)
            if(ind1 == ind2):
                ind2 += 1
            cxpoint1 = random.randint(0, size)
            cxpoint2 = random.randint(0, size - 1)
            if(cxpoint2 >= cxpoint1):
                cxpoint2 += 1
            else: # Swap the two cx points
                cxpoint1, cxpoint2 = cxpoint2, cxpoint1

            point_set.append(ind1)
            point_set.append(ind2)
            point_set.append(cxpoint1)
            point_set.append(cxpoint2)

            if(i != 0):
                if(point_set in t_list):
                    point_set.clear()
                else:
                    t_list.append(copy.deepcopy(point_set))
                    point_set.clear()
                    break
            else:
                t_list.append(copy.deepcopy(point_set))
                point_set.clear()
                break
       
        excluded.extend(request[ind1])
        excluded.extend(request[ind2])
        excluded.extend(other[ind1])
        excluded.extend(other[ind2])

        for s in range(30):
            if(s  not in excluded):
                if(s < cxpoint1):
                    copy2[ind1][s],copy2[ind2][s] = copy2[ind2][s],copy2[ind1][s]
                elif(s == cxpoint1):
                    copy2[ind1][s],copy2[ind2][s] = copy2[ind2][s],copy2[ind1][s]
                    copy1[ind1][s],copy1[ind2][s] = copy1[ind2][s],copy1[ind1][s]
                elif(s > cxpoint1 and s < cxpoint2):
                    copy1[ind1][s],copy1[ind2][s] = copy1[ind2][s],copy1[ind1][s]
                elif(s == cxpoint2):
                    copy2[ind1][s],copy2[ind2][s] = copy2[ind2][s],copy2[ind1][s]
                    copy1[ind1][s],copy1[ind2][s] = copy1[ind2][s],copy1[ind1][s]
                elif(s > cxpoint2):
                    copy2[ind1][s],copy2[ind2][s] = copy2[ind2][s],copy2[ind1][s]
        
        excluded.clear()

        #copy1[ind1][cxpoint1:cxpoint2], copy1[ind2][cxpoint1:cxpoint2] = copy1[ind2][cxpoint1:cxpoint2], copy1[ind1][cxpoint1:cxpoint2]
        ind_list.append(copy1)
        #copy2[ind1][0:cxpoint1+1], copy2[ind2][0:cxpoint1] = copy2[ind2][0:cxpoint1], copy2[ind1][0:cxpoint1]
        #copy2[ind1][cxpoint2:size], copy2[ind2][cxpoint2:size] = copy2[ind2][cxpoint2:size], copy2[ind1][cxpoint2:size]
        ind_list.append(copy2)
    
    t_list.clear()
    return ind_list

origine = []

def my_index_multi(l, x):
    return [i for i, _x in enumerate(l) if _x == x]

def mut(individual):
    global origine

    x = cal_p(individual)
    y = cal_p(origine)

    if(x < y):
        ind = copy.deepcopy(individual)
    elif(x > y):
        ind = copy.deepcopy(origine)
    else:
        ind = copy.deepcopy(individual)

    origine = ind

    j = random.randint(0,29)
    

    while(1):
        k = random.randint(0,24)
        i = random.randint(0,24)
        if(i != k and ind[k][j] <= 3 and ind[i][j] <= 3):
            break
    ind[i][j],ind[k][j] = ind[k][j],ind[i][j]
    
    day = ind[:,j]

    d = np.sum(ind[:,j] == 1)
    f = np.sum(ind[:,j] == 0)
    count = 0

    f_list = np.where(day == 0)
    d_list = np.where(day == 1)
    if((len(f_list[0]) - 1) >= 1 and (len(d_list[0]) - 1) >= 1):
        while(1):
            count += 1
            r = random.randint(0,1)
            if(r == 0 and f > min_num_f[j] and f <= max_num_f[j] and (d + 1) <= max_num_d[j]):
                z = f_list[0][np.random.randint(0,len(f_list[0]))]
                ind[z][j] = 1
                break
            elif(r == 1 and d > min_num_d[j] and d <= max_num_d[j] and (f + 1) <= max_num_f[j]):
                z = d_list[0][np.random.randint(0,len(d_list[0]))]
                ind[z][j] = 0
                break
            elif(count == 10):
                break

    return ind

def cal_p(pop): 
    num2 = employee_num(pop) 
    num3 = ShiftPattern(pop)
    
    penalty = num2 + (num3 * 100)

    return penalty

def cal_enum(pop):
    num2 = employee_num(pop) 
    num3 = ShiftPattern(pop)

    return num2,num3


def evalshift(pop):
    penalty = cal_p(pop)
    return penalty,

def result(pop):
    d = np.sum(pop == 1, axis = 0)
    e = np.sum(pop == 2, axis = 0)
    n = np.sum(pop == 3, axis = 0)
    f = np.sum(pop == 0, axis = 0)
    f += np.sum(pop == 5, axis = 0)
    for num,ind in enumerate(pop):
        print("%2d:" % num ,end = "")
        print(ind)
    print(cal_p(pop))
    print()

    """for j in range(30):
        for s in pop:
            day.append(s.shift[j])
        d[j] = day.count(1)
        e[j] = day.count(2)
        n[j] = day.count(3)
        f[j] = day.count(0) + day.count(5)
        day.clear()"""

    print(d)
    print(e)
    print(n)
    print(f)

    g1 = A.error(pop)
    g2 = A_SS.error(pop)
    g3 = B.error(pop)
    g4 = B_SS.error(pop)
    g5 = B_SS_s.error(pop)
    g6 = B_rq_s.error(pop)
    g7 = o_n.error(pop)
    g8 = all_shift.error(pop)

    p3 = ShiftPattern(pop)

    """for i,ind in enumerate(pop):
        d = ind.shift.count(1)
        e = ind.shift.count(2)
        n = ind.shift.count(3)
        f = ind.shift.count(0) + ind.shift.count(5)
        p3.append(str(i))
        p3.append(str(d))
        p3.append(str(e))
        p3.append(str(n))
        p3.append(str(f))

        map_l = map(str,ind.shift)
        pattern = ''.join(map_l)
        for x in b_shift:
            y = re.findall(x,pattern)
            p3.append(y)
            p3.append(str(len(y)))
        print(p3)
        p3.clear()"""
    
    print("g1:",end = "")
    print(g1)
    print("g2:",end = "")
    print(g2)
    print("g3:",end = "")
    print(g3)
    print("g4:",end = "")
    print(g4)
    print("g5:",end = "")
    print(g5)
    print("g6:",end = "")
    print(g6)
    print("g7:",end = "")
    print(g7)
    print("g8:",end = "")
    print(g8)

    print("p3:",end = "")
    print(p3)

def create_pop():
    ind = np.empty((25,30), int)
    for i in range(25):
        for j in range(30):
            r = np.random.randint(0,4)
            ind[i][j] = r
    return ind

def simulated_annealing(pop):
    population = copy.deepcopy(pop)
    j = random.randint(0,29)
    day = population[:,j]
    d = np.sum(population[:,j] == 1)
    f = np.sum(population[:,j] == 0)
    count = 0

    f_list = np.where(day == 0)
    d_list = np.where(day == 1)
    if((len(f_list[0]) - 1) >= 1 and (len(d_list[0]) - 1) >= 1):
        while(1):
            count += 1
            r = random.randint(0,1)
            if(r == 0 and f > min_num_f[j] and f <= max_num_f[j] and (d + 1) <= max_num_d[j]):
                z = f_list[0][np.random.randint(0,len(f_list[0]))]
                population[z][j] = 1
                break
            elif(r == 1 and d > min_num_d[j] and d <= max_num_d[j] and (f + 1) <= max_num_f[j]):
                z = d_list[0][np.random.randint(0,len(d_list[0]))]
                population[z][j] = 0
                break
            elif(count == 10):
                break
    
    prob = LocalSearch(population)
    prob.steps = 20000
    prob.copy_strategy = "deepcopy"
    prob.anneal()

    print("\n--------Simulated Annealing----------")
    print("best_energy:",end = "")
    print(prob.best_energy)

    return prob.best_state

toolbox = base.Toolbox()
toolbox.register("map", futures.map)
#0:休暇 1:日勤 2:準夜勤 3:夜勤 4:その他
toolbox.register("attr_bool", random.randint, 0,3)
toolbox.register("gene", tools.initRepeat, list , toolbox.attr_bool, 30)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.gene,25)
toolbox.register("population",tools.initRepeat,list,toolbox.individual)
toolbox.register("evaluate",evalshift)
toolbox.register("mate", cxTwoPoint)
toolbox.register("mutate", mut)
#toolbox.register("mutate", mut)
#toolbox.register("select", tools.selTournament, tournsize=3)

def main():
    global origine
    start = time.time()
    pop = create_pop()
    NGEN = 50000
    m = 10
    c = 0

    print("Start of evolution")
        
    pop = Shift_init(pop)

    fits1 = cal_p(pop)
    origine = pop
    fits2 = fits1
    best_fits = fits1
    best_pop = copy.deepcopy(pop)
    result(pop)

    for g in range(NGEN):
       
        print("-- Generation %i --" % g)
        offspring = pop

        ind_list = toolbox.mate(offspring)
        fitnesses = Parallel(n_jobs=-1)( [delayed(cal_p)(ind) for ind in ind_list])
        i = fitnesses.index(min(fitnesses))

        best_ind = ind_list[i]
        
        if(g % m == 0):
            best_ind = toolbox.mutate(best_ind)
            c += 1
            if(c == 60):
                m += 20
                c = 0

        pop[:] = best_ind

        fits1 = cal_p(pop)

        if(fits1 == fits2):
            count += 1
        else:
            count = 0
        
        fits2 = fits1

        if(count == 50):
            pop = simulated_annealing(pop)
            fits1 = cal_p(pop)
            count = 0

        num2,num3 = cal_enum(pop)
        print("fits1 = %f" % fits1)
        print("enum2 = %f" % num2)
        print("enum3 = %f" % num3)
        ind_list.clear()

        if(fits1 == 0):
            break

        if(best_fits > fits1):
            best_fits = fits1
            best_pop = copy.deepcopy(pop)
            origine = copy.deepcopy(best_pop)
            best_generation = g

    print("-- End of (successful) evolution --")
    print("Best individual is ")
    print("Generation %d" % best_generation)
    result(best_pop)
    elapsed_time = (time.time() - start) / 3600 
    print("elapsed_time:{0}".format(elapsed_time) + "[h]")

    s = r"C:\Users\owner\Desktop\Research\output\csv" + "\\"
    fname = s + datetime.now().strftime("%Y%m%d_%H%M%S") 
    f = open(fname + '.csv',mode = 'w')
    writer_d = csv.writer(f,lineterminator = '\n')
    for i,data in enumerate(best_pop):
        x = np.insert(data,0,i + 1)
        writer_d.writerow(x)
    f.close()

    """f1name = s + "error_list.csv"
    f1 = open(f1name,"w")
    write = csv.writer(f1,lineterminator = '\n')
    A.save(write)
    A_SS.save(write)
    B.save(write)
    B_SS.save(write)
    B_SS_s.save(write)
    B_rq_s.save(write)
    o_n.save(write)
    all_shift.save(write)"""

if __name__ == '__main__':
    main()