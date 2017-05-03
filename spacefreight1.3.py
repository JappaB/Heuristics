'''
Heuristieken blok 5 2016-2017
Space Freight opdracht B

Jasper Bakker (10260250)
Sanne Berendschot (10269290)
Laurens vd Ziel (10653384)

'''

# Import packages
import random
import json
import os
from operator import itemgetter
import sortingmethods as sortmeth
import information as inf


# Global variables
# Declare dict with spacecraft names (as objects)
spacecraftsDict = {}
# Comment: pas hier aan hoeveel iteraties je HC of SA wilt laten doen Number of iterations for HC and SA algorithm
ITERATIONS = 5
# comment : wilde onderstaande gebruiken om te meten hoe goed het ging, maar na me een klein beetje verdiept te hebben in logging denk ik dat dat slimmer is.
#List to remember the various configurations of the HC and SA algorithm
m3OnGroundList = []


# Create classes for spacecrafts
class Spacecraft(object):

	# Lukt niet om dit goed over te dragen op de children classes

	def __init__(self, name, spaceleft, kgsleft, density, country):
		self.name = name
		self.spaceleft = spaceleft
		self.kgsleft = kgsleft
		self.density = kgsleft / spaceleft
		self.country = country

	def displaySpacecraft(self):
		print ("name: ", self.name, ", Spaceleft: ", self.spaceleft, ", Kgsleft: ", self.kgsleft, ", Densityleft: ", self.density, ", Coutry: ", self.country)

class Cygnus(Spacecraft):

	#name = 'Cygnus'
	def __init__(self, name='Cygnus', spaceleft=18.9, kgsleft=2000, density=0, country='USA'):
		Spacecraft.__init__(self, name, spaceleft, kgsleft, density, country)

class VerneATV(Spacecraft):

	#name = 'Cygnus'
	def __init__(self, name='VerneATV', spaceleft=13.1, kgsleft=2300, density=0, country='Europe'):
		Spacecraft.__init__(self, name, spaceleft, kgsleft, density, country)

class Progress(Spacecraft):

	#name = 'Cygnus'
	def __init__(self, name='Progress', spaceleft=7.6, kgsleft=2400, density=0, country='Russia'):
		Spacecraft.__init__(self, name, spaceleft, kgsleft, density, country)

class Kounotori(Spacecraft):

	#name = 'Cygnus'
	def __init__(self, name='Kounotori', spaceleft=14, kgsleft=5200, density=0, country='Japan'):
	 	Spacecraft.__init__(self, name, spaceleft, kgsleft, density, country)

def main():

	# Logging: https://fangpenlin.com/posts/2012/08/26/good-logging-practice-in-python/
	# or maybe http://www.patricksoftwareblog.com/python-logging-tutorial/

	logger = logging.getLogger(__name__)
	logging.basicConfig(level=logging.INFO)
	logging.info('Start reading database')
	# read database here
	records = {'john': 55, 'tom': 66}
	logger.debug('Records: %s', records)
	logger.info('Updating records ...')
	# update records here
	logger.info('Finish updating records')


	# setupLogging()

	# Make spacecrafts
	Cygnus1 = Cygnus()
	spacecraftsDict["Cygnus1"] = Cygnus1
	VerneATV1 = VerneATV()
	spacecraftsDict["VerneATV1"] = VerneATV1
	Progress1 = Progress()
	spacecraftsDict["Progress1"] = Progress1
	Kounotori1 = Kounotori()
	spacecraftsDict["Kounotori1"] = Kounotori1

	print (spacecraftsDict)

	with open('Cargolist1.json') as cargolistFile1:    
	    cargolist1 = json.load(cargolistFile1)

		### SORT CARGOLIST ###
	# Unpack
	cargolist1 = sortmeth.unpack(cargolist1)

	# Weight
	# cargolist1 = sortmeth.sortWeight(cargolist1)

	# Density
	cargolist1 = sortmeth.sortDensity(cargolist1)

	# Random
	# cargolist1 = sortmeth.sortRandom(cargolist1)
	


	# cargoOnlyWeightLeftAircraft(cargolist1)
	cargoMostDensityLeftAircraft(cargolist1)
	# cargoRandom(cargolist1)

	#inf.infoCargoGround(cargolist1)

	# Display Spacecrafts
	for Spacecraft in spacecraftsList:
		Spacecraft.displaySpacecraft()

	#hillClimber(cargolist1, spacecraftsList)





# Algorithm to pack cargolist on most weight left
def cargoOnlyWeightLeftAircraft (cargolist):

	# for every package in cargolist
	for cargo in cargolist:

		# sorteer locatielijst op gewichtscapaciteit er over is
		spacecraftsList.sort(key = lambda k: k.kgsleft, reverse = True)
	
		# if possible, put cargo in spacecraft following a given order
		putCargoinSpacecraftinthefollowingOrder(cargo, spacecraftsList)



# Algorithm to pack cargolist on most density left
def cargoMostDensityLeftAircraft (cargolist):

	# voor elk pakketje in de lijst
	for cargo in cargolist:

		# sort list with available spacecrafts on the density of the capacity that is left
		spacecraftsList.sort(key = lambda k: k.density, reverse = True)
		
		# if possible, put cargo in spacecraft following a given order
		putCargoinSpacecraftinthefollowingOrder(cargo, spacecraftsList)

def cargoRandom (cargolist):

	for cargo in cargolist:

		# sort list with available spacecrafts randomly
		random.shuffle(spacecraftsList)

		# if possible, put cargo in spacecraft following a given order
		putCargoinSpacecraftinthefollowingOrder(cargo, spacecraftsList)

def putCargoinSpacecraftinthefollowingOrder (cargo, spacecraftsList): 

	for spacecraft in spacecraftsList:

		# check of er genoeg plek is om het pakketje te plaatsen 
		if spacecraft.kgsleft >= cargo['kgs'] and spacecraft.spaceleft >= cargo['m3']:

			# zet het pakketje in de minst volle spacecrafts
			# Comment voor iedereen: als we zometeen een lijst hebben met meerdere spacecrafts, dan kun je niet selecteren
			# op naam en al helemaal niet op country (meerdere spacecrafts uit 1 land zometeen) van een bepaald spacecraft, dan moeten we selecteren op id
			cargo['location'] = spacecraft.country

			# update de locatie over van de spacecrafts
			spacecraft.kgsleft -= cargo['kgs']
			spacecraft.spaceleft -= cargo['m3']
			break

# def hillClimber (cargolist, spacecraftsList):

# 	'''
# 	This Hillclimber Algorithm accepts new situations as better when:
# 	- There is less m3 or kg left on the ground
# 	- The trade was between spacecrafts and the spacecraft that innitially had 
# 	more space (m3) or more kg left, now has even more space or kg left.
# 	(so that a (larger) package from the ground might fit in this spacecraft now)

# 	LET OP: Random function generates pseudo-random numbers. Hij is snel en efficient, maar niet goed genoeg voor 
# 	bijvoorbeeld wachtwoorden
# 	(https://docs.python.org/2/library/random.html)

# 	'''
# 	# Objectives can be m3 or kg in this algorithm
# 	objective = "m3"

# 	# Number of swaps
# 	# Run hillclimber x times
# 	for i in range (ITERATIONS):

# 			# Comment voor Laurens:
# 			# gebruik == ipv is (zie bijvoorbeeld het bestand 'information.py')
# 			# is er een reden waarom je daar is gebruikt ipv ==?
# 			# http://stackoverflow.com/questions/2209755/python-operation-vs-is-not

# 			# Randomly pick two cargo items from the cargolist
# 			swapped1 = random.choice(cargolist)
# 			swapped2 = random.choice(cargolist)

# 			# If both are on the ground, pick new random cargo
# 			if (swapped1['location'] == 'Ground' and swapped2['location'] == 'Ground'):
# 				break

# 			# If one of the two is on the ground and the other in the spacecraft
# 			# http://stackoverflow.com/questions/7141208/python-simple-if-or-logic-statement
# 			if (swapped1['location'] != 'Ground' and swapped2['location'] == 'Ground'):

# 				# If the package on the ground is larger and there is enough room (in kg and m3) to swap, then swap


# 				# Comment voor iedereen, of ik de spacecraftlist nou als dict of als list doe, ik krijg de onderstaande regel nog niet werkend.
# 				# Wellicht is het een idee om de objecten in de cargolist te storen. Dan kun je gewoon binnen de dictionairy van een cargo-item 
# 				#
# 				if (swapped1[objective] < swapped2[objective] and (spacecraftsDict[swapped1['location']].kgsleft >= (swapped2['kgs']-swapped1['kgs']) and spacecraftsDict[swapped1['location']].spaceleft >= (swapped2['m3']-swapped1['m3'])):
					
# 					# Comment voor iedereen: Misschien later nog een all-purpose swap functie maken, we doen dit meerdere keren maar de
# 					# putcargoinspacecraft function is niet algemeen genoeg voor deze functie

# 					# How to swap in Python:
# 					# http://stackoverflow.com/questions/14836228/is-there-a-standardized-method-to-swap-two-variables-in-python
# 					swapped1['location'], swapped2['location'] = swapped2['location'], swapped1['location']

# 					# Update spacecraft 
# 					'''
# 					Pseudecode:
# 					kgsleft of spacecraft of swapped1 decrease by (swapped2(kgs)-swapped1(kgs))
# 					spaceleft of spacecraft of swapped1 decrease by (swapped2(m3)-swapped1(m3))

# 					'''

# 					# Log the configuration of the location of all cargo (comment: daarmee kunnen we vervolgens alles berekenen wat we willen) and which iteration this was




# 			if (swapped1['location'] == 'Ground' and swapped2['location'] != 'Ground'):		


# 			# If both are in spacecraft
# 			if (swapped1['location'] != 'Ground' and swapped2['location'] != 'Ground'):

			




### RUN PROGRAM ###
if __name__ == '__main__':
	main()
	