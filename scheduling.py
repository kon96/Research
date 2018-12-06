import random
import sys
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

def mut(individual,indpb):
    for i in range(len(individual)):
        for j in range(len(individual[i])):
            if random.random() <indpb:
                individual[i][j] = random.randint(0,3)

    return individual,

def evalOneMin(individual):
    return sum(individual),

def evalshift(pop):
    num1,num2 = employee_num(pop) 
    return (num1,num2)

creator.create("FitnessShift", base.Fitness, weights=(-1.0,-2.0))
creator.create("Individual", list, fitness = creator.FitnessShift)

toolbox = base.Toolbox()
toolbox.register("map", futures.map)

#0:休暇 1:日勤 2:準夜勤 3:夜勤 4:その他
toolbox.register("attr_bool", random.randint, 0,3)
toolbox.register("gene", tools.initRepeat, list , toolbox.attr_bool, 30)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.gene,25)
toolbox.register("population",tools.initRepeat,list,toolbox.individual)
toolbox.register("evaluate",evalshift)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", mut, indpb = 0.05)
#toolbox.register("mutate", mut)
toolbox.register("select", tools.selTournament, tournsize=3)

def main():
    pop = toolbox.population(n = 150)
    CXPB, MUTPB, NGEN = 0.8, 0.2, 1000

    print("Start of evolution")
    #for i in range(len(pop)):
     #   nurse.append(Employee(i + 1,[],False))
        

    fitness = list(map(toolbox.evaluate, pop))
    for ind, fit in zip(pop,fitness):
        ind.fitness.values = fit

    print(" Evaluating %i individuals" % len(pop))

    for g in range(NGEN):
        if(g % 200 == 0):
            NGEN -= 0.01
        print("-- Generation %i --" % g)

        offspring = toolbox.select(pop,len(pop))
        offspring = list(map(toolbox.clone, offspring))

        j = 0

        #for shift in offspring:
           # nurse[j].shift = shift
           # j += 1

        for child1 ,child2 in zip(offspring[::2],offspring[1::2]):
            if random.random() < CXPB:
                for gene1, gene2 in zip(child1[::2],child2[1::2]):
                    toolbox.mate(gene1,gene2)
                    del child1.fitness.values
                    del child2.fitness.values
        
        for mutant in offspring:
            if random.random() < MUTPB:
                #toolbox.mutate(mutant,MUTPB)
                toolbox.mutate(mutant)
                del mutant.fitness.values

        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        fitnesses = map(toolbox.evaluate, invalid_ind)

        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit

        print(" Evaluated %i individuals" % len(invalid_ind))

        pop[:] = offspring

        fits1 = [ind.fitness.values[0] for ind in pop]
        fits2 = [ind.fitness.values[1] for ind in pop]

        length = len(pop)
        mean1 = sum(fits1) /length
        mean2 = sum(fits2) /length
        sum1 = sum(x*x for x in fits1)
        sum2 = sum(x*x for x in fits2)
        std1 = abs(sum1 / length - mean1**2)**0.5
        std2 = abs(sum2 / length - mean2**2)**0.5

        print("  Min1 %s" % min(fits1))
        print("  Max1 %s" % max(fits1)) 
        print("  Avg1 %s" % mean1)
        print("  Std1 %s" % std1)
        print("")
        print("  Min2 %s" % min(fits2))
        print("  Max2 %s" % max(fits2))
        print("  Avg2 %s" % mean2)
        print("  Std2 %s" % std2)

        if(min == 0):
            break

    print("-- End of (successful) evolution --")
    
    best_ind = tools.selBest(pop, 1)[0]
    print("Best individual is ")
    for ind in best_ind:
        print(ind)
    print(best_ind.fitness.values)
    result(best_ind)

if __name__ == '__main__':
    main()


