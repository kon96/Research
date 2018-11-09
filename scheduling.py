
import random
import sys
sys.path.append('/usr/local/lib/python3.6/dist-packages')

from scoop import futures
from deap import base
from deap import creator
from deap import tools
from deap import cma

class Employee(object):
  def __init__(self, no, shift, manager):
    self.no = no
    self.manager = manager
    self.shift = shift

creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()

toolbox.register("map", futures.map)

toolbox.register("attr_bool", random.randint, 0,3)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, 31)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

def mut(individual,indpb):
    for i in range(len(individual)):
        if random.random() <indpb:
            individual[i] = random.randint(0,3)

    return individual,

def evalOneMin(individual):
    return sum(individual),

toolbox.register("evaluate",evalOneMin)

toolbox.register("mate", tools.cxTwoPoint)

toolbox.register("mutate", mut, indpb=0.05)

toolbox.register("select", tools.selTournament, tournsize=3)

def main():
    pop = toolbox.population(n = 25)
    CXPB, MUTPB, NGEN = 0.5, 0.2, 40
    nurse = []

    print("Start of evolution")
    for i in range(len(pop)):
        nurse.append(Employee(i + 1,[],False))
        

    fitness = list(map(toolbox.evaluate, pop))
    for ind, fit in zip(pop,fitness):
        ind.fitness.values = fit

    print(" Evaluating %i individuals" % len(pop))

    for g in range(NGEN):
        print("-- Greneration %i --" % g)

        offspring = toolbox.select(pop,len(pop))
        offspring = list(map(toolbox.clone, offspring))

        j = 0

        for shift in offspring:
            nurse[j].shift = shift
            j += 1

        for child1 ,child2 in zip(offspring[::2],offspring[1::2]):
            if random.random() <CXPB:
                toolbox.mate(child1,child2)
                del child1.fitness.values
                del child2.fitness.values
        
        for mutant in offspring:
            if random.random() < MUTPB:
                toolbox.mutate(mutant)
                del mutant.fitness.values

        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        fitnesses = map(toolbox.evaluate, invalid_ind)
        f_list = list(fitnesses)

        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit

        print(" Evaluated %i individuals" % len(invalid_ind))

        pop[:] = offspring

        fits = [ind.fitness.values[0] for ind in pop]

        length = len(pop)
        mean = sum(fits) /length
        sum2 = sum(x*x for x in fits)
        std = abs(sum2 / length - mean**2)**0.5

        print("  Min %s" % min(fits))
        print("  Max %s" % max(fits))
        print("  Avg %s" % mean)
        print("  Std %s" % std)

    print("-- End of (successful) evolution --")
    
    best_ind = tools.selBest(pop, 1)[0]
    print("Best individual is %s, %s" % (best_ind, best_ind.fitness.values))

if __name__ == '__main__':
    main()
 


