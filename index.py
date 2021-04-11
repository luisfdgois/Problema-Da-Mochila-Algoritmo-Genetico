import random
import matplotlib.pyplot
from deap import creator, base, tools, algorithms

def GenerateItems(size):
    itens = []
    itens.append({"Weight": 0, "Value": 0})
    for indice in range(size - 2):
        weight = random.randint(1, 5)
        value = random.randint(weight, (weight + 5))
        itens.append({"Weight": weight, "Value": value})
    itens.append({"Weight": 0, "Value": 0})
    return itens

def CalculateWeight(individual, listItems):
  weight = 0
  for ind in individual:
    weight += listItems[ind].get("Weight")
  return weight

def CalculateAmount(individual, listItems):
  amount = 0
  for ind in individual:
    amount += listItems[ind].get("Value")
  return amount

INDIVIDUAL_SIZE = 10
BACKPACK_WEIGHT = 30
POPULATION_SIZE = 300
MAX_INTERACTION_COUNT = 10
MAX_VARIATION = 2
NUMBER_ITEMS = 10
LIST_REFERENCES = GenerateItems(NUMBER_ITEMS)
VARIATION_SIZE = 3
LIST_BESTINDIVIDUAL_WEIGHT = []
LIST_BESTINDIVIDUAL_AMOUNT = []


creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

toolbox = base.Toolbox()

toolbox.register("attribute_int", random.randint, 0, (NUMBER_ITEMS - 1))
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attribute_int, INDIVIDUAL_SIZE)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)


def evaluationFunction(individual):
    fit = 0
    weight = 0
    for ind in individual:
        fit += LIST_REFERENCES[ind].get("Value", 0)
        weight += LIST_REFERENCES[ind].get("Weight", 0)
        if weight > BACKPACK_WEIGHT:
            return 0
    return fit

toolbox.register("evaluate", evaluationFunction)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutUniformInt, low=0, up=(NUMBER_ITEMS - 1), indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=VARIATION_SIZE)

population = toolbox.population(n=POPULATION_SIZE)

bestSolution = {"fit": 0, "ind": None}

evolutionCount = 0

while evolutionCount < MAX_INTERACTION_COUNT:

    offspring = algorithms.varAnd(population, toolbox, cxpb=0.5, mutpb=0.1)

    fits = toolbox.map(toolbox.evaluate, offspring)

    bestIndividual = {"fit": 0, "ind": None}

    for fit, ind in zip(fits, offspring):
        ind.fitness.values = (fit),
        if fit > bestIndividual.get("fit", 0):
            bestIndividual = {"fit": fit, "ind": ind}

    population = toolbox.select(offspring, k=len(population))

    bestIndividualFit = bestIndividual.get("fit")
    bestFit = bestSolution.get("fit")

    if ((bestIndividualFit >= bestFit and (bestIndividualFit <= bestFit + MAX_VARIATION)) or 
        ((bestIndividualFit < bestFit and bestIndividualFit >= bestFit - MAX_VARIATION))):
        evolutionCount += 1
    else:
        evolutionCount = 0

    bestSolution = (bestFit > bestIndividualFit) and bestSolution or bestIndividual

    LIST_BESTINDIVIDUAL_AMOUNT.append(CalculateAmount(bestSolution.get("ind"), LIST_REFERENCES))
    LIST_BESTINDIVIDUAL_WEIGHT.append(CalculateWeight(bestSolution.get("ind"), LIST_REFERENCES))

# Print dos itens disponíveis
for item in range(len(LIST_REFERENCES)):
  print(item, " - ", LIST_REFERENCES[item])

# Print do gráfico da evolução
matplotlib.pyplot.ylabel('PESOS')
matplotlib.pyplot.xlabel('VALOR TOTAL')
matplotlib.pyplot.ylim((min(LIST_BESTINDIVIDUAL_WEIGHT) - 10), (BACKPACK_WEIGHT + 10))
matplotlib.pyplot.plot(LIST_BESTINDIVIDUAL_AMOUNT, LIST_BESTINDIVIDUAL_WEIGHT)
matplotlib.pyplot.show()
