import random
import sys
import re
sys.path.append('/usr/local/lib/python3.6/dist-packages')

from scoop import futures
from deap import base
from deap import creator
from deap import tools
from deap import cma

#ALL
max_num_d = [11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,18,11,11,11,11,11,11,11]
min_num_d = [8,8,8,8,7,8,8,8,7,7,7,7,7,8,8,8,8,8,7,8,8,8,13,8,8,7,8,8,8,8]
max_num_e = [4 for i in range(30)]
min_num_e = [4 for i in range(30)]
max_num_n = [3 for i in range(30)]
min_num_n = [3 for i in range(30)]

#1-9 = 1,9
g_1_9 = [1,9]
max_num_1_9_d = [2 for i in range(30)]
min_num_1_9_d = [0 for i in range(30)]
max_num_1_9_e = [1 for i in range(30)]
min_num_1_9_e = [0 for i in range(30)]
max_num_1_9_n = [1 for i in range(30)]
min_num_1_9_n = [0 for i in range(30)]

#A_SS = 1,2,3,4,5,6
g_A_SS = [1,2,3,4,5,6]
max_num_A_SS_d = [2,3,3,3,2,3,2,3,2,2,2,2,2,2,3,2,2,3,2,2,3,3,6,2,2,2,3,3,3,2]
min_num_A_SS_d = [2 for i in range(30)]
max_num_A_SS_e = [1 for i in range(30)]
min_num_A_SS_e = [1 for i in range(30)]
max_num_A_SS_n = [1 for i in range(30)]
min_num_A_SS_n = [1 for i in range(30)]

#B_rq_s = 19,20,21,22,23,24,25
g_B_rq_s = [19,20,21,22,23,24,25]
max_num_B_rq_s_d = [4,6,6,6,4,6,4,6,4,4,4,4,4,4,6,4,4,6,4,4,5,6,6,4,4,4,6,6,6,4]
min_num_B_rq_s_d = [2 for i in range(30)]
max_num_B_rq_s_e = [1 for i in range(30)]
min_num_B_rq_s_e = [1 for i in range(30)]
max_num_B_rq_s_n = [2 for i in range(30)]
min_num_B_rq_s_n = [0 for i in range(30)]

#B_SS = 14,15,16,17,18
g_B_SS = [14,15,16,17,18]
max_num_B_SS_d = [2,3,3,3,2,3,2,3,1,1,1,2,1,2,3,2,2,3,2,1,3,3,6,2,2,2,3,3,3,2]
min_num_B_SS_d = [1,1,1,1,1,1,1,1,0,0,0,1,0,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1]
max_num_B_SS_e = [1 for i in range(30)]
min_num_B_SS_e = [1 for i in range(30)]
max_num_B_SS_n = [1 for i in range(30)]
min_num_B_SS_n = [0 for i in range(30)]

#B_SS_s = 14,15,16,17,18,25
g_B_SS_s = [14,15,16,17,18,25]
max_num_B_SS_s_d = [3,3,3,3,2,3,3,3,2,2,2,2,2,3,3,3,3,3,2,2,3,3,6,3,3,2,3,3,3,3]
min_num_B_SS_s_d = [2,2,2,2,2,2,2,2,1,1,1,2,1,2,2,2,2,2,2,1,2,2,2,2,2,2,2,2,2,2]
max_num_B_SS_s_e = [2 for i in range(30)]
min_num_B_SS_s_e = [1 for i in range(30)]
max_num_B_SS_s_n = [1 for i in range(30)]
min_num_B_SS_s_n = [1 for i in range(30)]

#GroupA = 1,2,3,4,5,6,7,8,9,10,11,12,13
g_A = [1,2,3,4,5,6,7,8,9,10,11,12,13]
max_num_A_d = [6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,9,6,6,6,6,6,6,6]
min_num_A_d = [4,4,4,4,3,4,4,4,4,4,4,3,4,4,4,4,4,4,3,4,4,4,6,4,4,3,4,4,4,4]
max_num_A_e = [2 for i in range(30)]
min_num_A_e = [2 for i in range(30)]
max_num_A_n = [2 for i in range(30)]
min_num_A_n = [1 for i in range(30)]

#GroupB = 14,15,16,17,18,19,20,21,22,23,24,25
g_B = [14,15,16,17,18,19,20,21,22,23,24,25]
max_num_B_d = [6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,9,6,6,6,6,6,6,6]
min_num_B_d = [4,4,4,4,3,4,4,4,4,4,4,3,4,4,4,4,4,4,3,4,4,4,6,4,4,3,4,4,4,4]
max_num_B_e = [2 for i in range(30)]
min_num_B_e = [2 for i in range(30)]
max_num_B_n = [2 for i in range(30)]
min_num_B_n = [1 for i in range(30)]

#禁止勤務パターン
b_shift = ['[0][1-3][0]','[1-3]{7}','[0]{6}','[1]{8}',
           '[3][0-3][3]','[3][0-3]{2}[3]','[3][0-3]{3}[3]',
           '[3][0-3]{4}[3]','[3][0-3]{5}[3]','[3]{3}',
           '[1]{5}','[2]{4}','[3][1]','[3][2]','[2][1]',
           '[3][0][1]'
]

class Employee(object):
  def __init__(self, no, shift, manager):
    self.no = no
    self.manager = manager
    self.shift = shift

class Shift(object):
    penalty1 = 0
    def __init__(self,d_max,d_min,e_max,e_min,n_max,n_min):
        self.d_max = d_max
        self.d_min = d_min
        self.e_max = e_max
        self.e_min = e_min
        self.n_max = n_max
        self.n_min = n_min
        self.d = [0 for i in range(30)]
        self.e = [0 for i in range(30)]
        self.n = [0 for i in range(30)]
        self.f = [0 for i in range(30)]
    
    def ref(self):
        self.d = [0 for i in range(30)]
        self.e = [0 for i in range(30)]
        self.n = [0 for i in range(30)]
        self.f = [0 for i in range(30)]
        Shift.penalty1 = 0
    
    def count(self,shift,j):
        if(shift == 0):
            self.f[j] += 1
        elif(shift == 1):
            self.d[j] += 1
        elif(shift == 2):
            self.e[j] += 1
        elif(shift == 3):
            self.n[j] += 1
    
    def check(self,j):
        if(self.d_max[j] < self.d[j] or self.d_min[j] > self.d[j]):
            Shift.penalty1 += 1
        if(self.e_max[j] < self.e[j] or self.e_min[j] > self.e[j]):
            Shift.penalty1 += 1
        if(self.n_max[j] < self.n[j] or self.n_min[j] > self.n[j]):
            Shift.penalty1 += 1

class Shift_G(Shift):
    penalty2 = 0

    def __init__(self,d_max,d_min,e_max,e_min,n_max,n_min,group):
        Shift.__init__(self,d_max,d_min,e_max,e_min,n_max,n_min)
        self.group = group
    
    def ref(self):
        self.d = [0 for i in range(30)]
        self.e = [0 for i in range(30)]
        self.n = [0 for i in range(30)]
        self.f = [0 for i in range(30)]
        Shift_G.penalty2 = 0

    def count(self,shift,j):
        if j in self.group:
            Shift.count(self,shift,j)
    
    def check(self,j):
        if(self.d_max[j] < self.d[j] or self.d_min[j] > self.d[j]):
            Shift_G.penalty2 += 1
        if(self.e_max[j] < self.e[j] or self.e_min[j] > self.e[j]):
            Shift_G.penalty2 += 1
        if(self.n_max[j] < self.n[j] or self.n_min[j] > self.n[j]):
            Shift_G.penalty2 += 1


all_shift = Shift(max_num_d,min_num_d,max_num_e,min_num_e,max_num_n,min_num_e)
o_n = Shift_G(max_num_1_9_d,min_num_1_9_d,max_num_1_9_e,min_num_1_9_e,max_num_1_9_n,min_num_1_9_e,g_1_9)
A = Shift_G(max_num_A_d,min_num_A_d,max_num_A_e,min_num_A_e,max_num_A_n,min_num_A_e,g_A)
A_SS = Shift_G(max_num_A_SS_d,min_num_A_SS_d,max_num_A_SS_e,min_num_A_SS_e,max_num_A_SS_n,min_num_A_SS_e,g_A_SS)
B = Shift_G(max_num_B_d,min_num_B_d,max_num_B_e,min_num_B_e,max_num_B_n,min_num_B_e,g_B)
B_SS = Shift_G(max_num_B_SS_d,min_num_B_SS_d,max_num_B_SS_e,min_num_B_SS_e,max_num_B_SS_n,min_num_B_SS_e,g_B_SS)
B_SS_s = Shift_G(max_num_B_SS_s_d,min_num_B_SS_s_d,max_num_B_SS_s_e,min_num_B_SS_s_e,max_num_B_SS_s_n,min_num_B_SS_s_e,g_B_SS_s)
B_rq_s = Shift_G(max_num_B_rq_s_d,min_num_B_rq_s_d,max_num_B_rq_s_e,min_num_B_rq_s_e,max_num_B_rq_s_n,min_num_B_rq_s_e,g_B_rq_s)

creator.create("FitnessShift", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness = creator.FitnessShift)

def result(pop):
    d = [0 for i in range(30)]
    e = [0 for i in range(30)]
    n = [0 for i in range(30)]
    f = [0 for i in range(30)]

    for i in range(len(pop)):
        for j in range(len(pop[i])):
            shift = pop[i][j]
            if(shift == 0):
                f[j] += 1
            elif(shift == 1):
                d[j] += 1
            elif(shift == 2):
                e[j] += 1
            elif(shift == 3):
                n[j] += 1

    print(d) 
    print(e)
    print(n)
    print(f)

def employee_num(pop):

    for i in range(len(pop)):
        for j in range(len(pop[i])):
            shift = pop[i][j]
            all_shift.count(shift,j)
            A.count(shift,j)
            A_SS.count(shift,j)
            B.count(shift,j)
            B_SS.count(shift,j)
            B_SS_s.count(shift,j)
            B_rq_s.count(shift,j)
            o_n.count(shift,j)
            
    for j in range(len(pop[i])):
        all_shift.check(j)
        A.check(j)
        A_SS.check(j)
        B.check(j)
        B_SS.check(j)
        B_SS_s.check(j)
        B_rq_s.check(j)
        o_n.check(j)

    p1 = Shift.penalty1
    p2 = Shift_G.penalty2

    all_shift.ref()
    A.ref()
    A_SS.ref()
    B.ref()
    B_SS.ref()
    B_SS_s.ref()
    B_rq_s.ref()
    o_n.ref()

    return p1, p2

def ShiftPattern(pop):
    penalty3 = 0
    for ind in pop:
        map_l = map(str,ind)
        pattern = ''.join(map_l)
        for x in b_shift:
            y = re.findall(x,pattern)
            penalty3 += len(y)
    
    return penalty3

def cxTwoPoint(pop):
   
    size = 30
    copy1 = creator.Individual()
    copy2 = creator.Individual()
    ind_list = []
    for i in range(50):
        copy1[:] = pop[:]
        copy2[:] = pop[:]
        ind1 = random.randint(0,24)
        ind2 = random.randint(0,23)
        if(ind1 == ind2):
            ind2 += 1
        cxpoint1 = random.randint(1, size)
        cxpoint2 = random.randint(1, size - 1)
        if cxpoint2 >= cxpoint1:
            cxpoint2 += 1
        else: # Swap the two cx points
            cxpoint1, cxpoint2 = cxpoint2, cxpoint1
        
        copy1[ind1][cxpoint1:cxpoint2], copy1[ind2][cxpoint1:cxpoint2] = copy1[ind2][cxpoint1:cxpoint2], copy1[ind1][cxpoint1:cxpoint2]
        ind_list.append(copy1)
        copy2[ind1][0:cxpoint1], copy2[ind2][cxpoint2:size] = copy2[ind2][0:cxpoint1], copy2[ind1][cxpoint2:size]
        ind_list.append(copy2)
        
    return ind_list

origine = creator.Individual()

def mut(individual):
    global origine
    if(toolbox.evaluate(individual) < toolbox.evaluate(origine)):
        ind = individual
    else:
        ind = origine
    origine = individual
    j = random.randint(1,30)
    while(1):
        i = random.randint(0,24)
        k = random.randint(0,24)
        if(i != k):
            break
    ind[i][j],ind[k][j] = ind[k][j],ind[i][j] 

    return ind

def evalshift(pop):
    num1,num2 = employee_num(pop) 
    num3 = ShiftPattern(pop)
    
    penalty = num1 + num2 + num3

    return penalty,

toolbox = base.Toolbox()
toolbox.register("map", futures.map)
#0:休暇 1:日勤 2:準夜勤 3:夜勤 4:その他
toolbox.register("attr_bool", random.randint, 0,3)
toolbox.register("gene", tools.initRepeat, list, toolbox.attr_bool, 30)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.gene,25)
toolbox.register("population",tools.initRepeat,list,toolbox.individual)
toolbox.register("evaluate",evalshift)
toolbox.register("mate", cxTwoPoint)
toolbox.register("mutate", mut)
#toolbox.register("mutate", mut)
toolbox.register("select", tools.selTournament, tournsize=3)

def main():
    global origine
    pop = toolbox.individual()
    origine = pop
    NGEN = 1000

    print("Start of evolution")
    #for i in range(len(pop)):
     #   nurse.append(Employee(i + 1,[],False))
        

    fitness = toolbox.evaluate(pop)
    print(" Evaluating %i individuals" % len(pop))

    for g in range(NGEN):
       
        print("-- Generation %i --" % g)

        offspring = pop
        offspring = list(map(toolbox.clone, offspring))

        #for shift in offspring:
           # nurse[j].shift = shift
           # j += 1

        ind_list = toolbox.mate(offspring)
        fitnesses = map(toolbox.evaluate,ind_list)

        for ind, fit in zip(ind_list, fitnesses):
            ind.fitness.values = fit

        best_ind = tools.selBest(ind_list, 1)[0]

        if(g % 200 == 0):
            best_ind = toolbox.mutate(best_ind)
            origine = best_ind

        pop[:] = best_ind
        pop.fitness.values = toolbox.evaluate(pop)

        fits1 = pop.fitness.values[0]

        print("fits1 = %f" % fits1)

        if(fits1 == 0):
            break

    print("-- End of (successful) evolution --")
    
    print("Best individual is ")
    for ind in pop:
        print(ind)
    result(pop)


if __name__ == '__main__':
    main()

