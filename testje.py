import json
from pyeasyga import pyeasyga
import sortingmethods as sortmeth

weightcap, volumecap = 5200, 14

# setup data
with open('cargolist1.json') as cargolist:   
   data = json.load(cargolist)

data = sortmeth.unpack(data)
data = sortmeth.sortDensity(data)
data = data[:30]

ga = pyeasyga.GeneticAlgorithm(data)        # initialise the GA with data
ga.population_size = 200                    # increase population size to 200 (default value is 50)

# define a fitness function
def fitness(individual, data):
   weight, volume, price = 0, 0, 0
   for (selected, item) in zip(individual, data):
      if selected:
         weight += item["kgs"]
         volume += item["m3"]
         price += item["m3"]
   if weight > weightcap or volume > volumecap:
      price = 0
   return price

ga.fitness_function = fitness               # set the GA's fitness function
ga.run()                                    # run the GA
print ga.best_individual()                  # print the GA's best solution