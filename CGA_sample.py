
import random
import sys
sys.path.append('/usr/local/lib/python3.6/dist-packages')

from scoop import futures
from deap import base
from deap import creator
from deap import tools
from deap import cma

#ALL
max_num_d = [11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,18,11,11,11,11,11,11,11]
min_num_d = [8,8,8,8,7,8,8,8,7,7,7,7,7,8,8,8,8,8,7,8,8,8,13,8,8,7,8,8,8,8]
max_num_e = [4 for i in range(30)]
min_num_e = [4 for i in range(30)]
max_num_n = [3 for i in range(30)]
min_num_n = [3 for i in range(30)]
max_num_f = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,5,10,10,10,10,10,10,10]
min_num_f = [7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,0,7,7,7,7,7,7,7]

#1-9 = 1,9
max_num_1_9_d = [2 for i in range(30)]
min_num_1_9_d = [0 for i in range(30)]
max_num_1_9_e = [1 for i in range(30)]
min_num_1_9_e = [0 for i in range(30)]
max_num_1_9_n = [1 for i in range(30)]
min_num_1_9_n = [0 for i in range(30)]

#A_SS = 1,2,3,4,5,6
max_num_A_SS_d = [2,3,3,3,2,3,2,3,2,2,2,2,2,2,3,2,2,3,2,2,3,3,6,2,2,2,3,3,3,2]
min_num_A_SS_d = [2 for i in range(30)]
max_num_A_SS_e = [1 for i in range(30)]
min_num_A_SS_e = [1 for i in range(30)]
max_num_A_SS_n = [1 for i in range(30)]
min_num_A_SS_n = [1 for i in range(30)]

#B_rq_s = 19,20,21,22,23,24,25
max_num_B_rq_s_d = [4,6,6,6,4,6,4,6,4,4,4,4,4,4,6,4,4,6,4,4,5,6,6,4,4,4,6,6,6,4]
min_num_B_rq_s_d = [2 for i in range(30)]
max_num_B_rq_s_e = [1 for i in range(30)]
min_num_B_rq_s_e = [1 for i in range(30)]
max_num_B_rq_s_n = [2 for i in range(30)]
min_num_B_rq_s_n = [0 for i in range(30)]

#B_SS = 14,15,16,17,18
max_num_B_SS_s_d = [2,3,3,3,2,3,2,3,1,1,1,2,1,2,3,2,2,3,2,1,3,3,6,2,2,2,3,3,3,2]
min_num_B_SS_s_d = [1,1,1,1,1,1,1,1,0,0,0,1,0,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1]
max_num_B_SS_s_e = [1 for i in range(30)]
min_num_B_SS_s_e = [1 for i in range(30)]
max_num_B_SS_s_n = [1 for i in range(30)]
min_num_B_SS_s_n = [0 for i in range(30)]

#B_SS_s = 14,15,16,17,18,25
max_num_1_9_d = [3,3,3,3,2,3,3,3,2,2,2,2,2,3,3,3,3,3,2,2,3,3,6,3,3,2,3,3,3,3]
min_num_1_9_d = [2,2,2,2,2,2,2,2,1,1,1,2,1,2,2,2,2,2,2,1,2,2,2,2,2,2,2,2,2,2]
max_num_1_9_e = [2 for i in range(30)]
min_num_1_9_e = [1 for i in range(30)]
max_num_1_9_n = [1 for i in range(30)]
min_num_1_9_n = [1 for i in range(30)]

#GroupA = 1,2,3,4,5,6,7,8,9,10,11,12,13
max_num_A_d = [6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,9,6,6,6,6,6,6,6]
min_num_A_d = [4,4,4,4,3,4,4,4,4,4,4,3,4,4,4,4,4,4,3,4,4,4,6,4,4,3,4,4,4,4]
max_num_A_e = [2 for i in range(30)]
min_num_A_e = [2 for i in range(30)]
max_num_A_n = [2 for i in range(30)]
min_num_A_n = [1 for i in range(30)]

#GroupB = 14,15,16,17,18,19,20,21,22,23,24,25
max_num_B_d = [6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,9,6,6,6,6,6,6,6]
min_num_B_d = [4,4,4,4,3,4,4,4,4,4,4,3,4,4,4,4,4,4,3,4,4,4,6,4,4,3,4,4,4,4]
max_num_B_e = [2 for i in range(30)]
min_num_B_e = [2 for i in range(30)]
max_num_B_n = [2 for i in range(30)]
min_num_B_n = [1 for i in range(30)]

d = [0 for i in range(30)]
e = [0 for i in range(30)]
n = [0 for i in range(30)]
f = [0 for i in range(30)]

class Employee(object):
  def __init__(self, no, shift, manager):
    self.no = no
    self.manager = manager
    self.shift = shift

def result(pop):
    global d
    global e
    global n
    global f

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

def employee_num(pop):
   
    global d
    global e
    global n
    global f

    penalty = 0

    
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
   
    for j in range(len(pop[i])):
        if(max_num_d[j] < d[j] or min_num_d[j] > d[j]):
                penalty += 1
        if(max_num_e[j] < e[j] or min_num_e[j] > e[j]):
            penalty += 1
        if(max_num_n[j] < n[j] or min_num_n[j] > n[j]):
            penalty += 1
        if(max_num_f[j] < f[j] or min_num_f[j] > f[j]):
            penalty += 1


    d = [0 for i in range(30)]
    e = [0 for i in range(30)]
    n = [0 for i in range(30)]
    f = [0 for i in range(30)]
    
    return penalty


creator.create("FitnessShift", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessShift)

toolbox = base.Toolbox()

toolbox.register("map", futures.map)

#0:休暇 1:日勤 2:準夜勤 3:夜勤 4:その他
toolbox.register("attr_bool", random.randint, 0,3)
toolbox.register("gene", tools.initRepeat, list , toolbox.attr_bool, 30)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.gene,25)
toolbox.register("population",tools.initRepeat,list,toolbox.gene)

def mut(individual,indpb):
    for i in range(len(individual)):
        if random.random() <indpb:
            individual[i] = random.randint(0,3)

    return individual,

def cxOne(s, pop, ind1, ind2):
    """Executes a one point crossover on the input :term:`sequence` individuals.
    The two individuals are modified in place. The resulting individuals will
    respectively have the length of the other.
    
    :param ind1: The first individual participating in the crossover.
    :param ind2: The second individual participating in the crossover.
    :returns: A tuple of two individuals.

    This function uses the :func:`~random.randint` function from the
    python base :mod:`random` module.
    """
    a = []
    b = []
    c = []
    d = []
    a[:] = ind1[:]
    b[:] = ind2[:]
    num = None

    min_f = list(toolbox.evaluate(pop))
    size = min(len(ind1), len(ind2))
    for i in range(1,size):
        c[:] = a[:]
        d[:] = b[:]
        c[i:], d[i:] = d[i:], c[i:]
        pop[s*2][:] = c[:]
        pop[s*2+1][:] = d[:]
        fitness = list(toolbox.evaluate(pop))
        if(fitness < min_f):
            min_f[0] = fitness[0]
            num = i
    if(num is not None):    
        ind1[num:], ind2[num:] = b[num:], a[num:]
    
    return ind1, ind2

def evalshift(pop):
    num = employee_num(pop) 
    return num,

toolbox.register("evaluate",evalshift)

toolbox.register("mate", cxOne)

toolbox.register("mutate", mut, indpb = 0.05)
#toolbox.register("mutate", mut)

toolbox.register("select", tools.selTournament, tournsize=3)

def main():
    global d
    global e
    global f
    global n
    pop = toolbox.population(n = 25)
    CXPB, MUTPB, NGEN = 0.8, 0.2, 1000

    print("Start of evolution")
    #for i in range(len(pop)):
     #   nurse.append(Employee(i + 1,[],False))
        

    fitness = toolbox.evaluate(pop)
    print(" Evaluating %i individuals" % len(pop))

    for g in range(NGEN):
        if(g % 200 == 0):
            NGEN -= 0.01
        print("-- Generation %i --" % g)

        offspring = pop
        offspring = list(map(toolbox.clone, offspring))

        j = 0

        #for shift in offspring:
           # nurse[j].shift = shift
           # j += 1

        for child1 ,child2 in zip(offspring[::2],offspring[1::2]):
            if random.random() < CXPB:
                toolbox.mate(j,offspring,child1,child2)
            j += 1
        
        for mutant in offspring:
            if random.random() < MUTPB:
                #toolbox.mutate(mutant,MUTPB)
                toolbox.mutate(mutant)

        fitnesses = toolbox.evaluate(pop)

        pop[:] = offspring

        print("fits = %d" % fitnesses)
        if(min == 0):
            break

    print("-- End of (successful) evolution --")
    
    print("Best individual is ")
    for ind in pop:
        print(ind)
    print(fitnesses)
    result(pop)
    print(d) 
    print(e)
    print(n)
    print(f)



if __name__ == '__main__':
    main()


