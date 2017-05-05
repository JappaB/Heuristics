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
import logging

# Global variables
# Declare dict with spacecraft names (as objects)
spacecraftsList = []
# Comment: pas hier aan hoeveel iteraties je HC of SA wilt laten doen Number of iterations for HC and SA algorithm
ITERATIONS = 1000000
# Dafualt Logging settings
defaultFormatter = logging.Formatter('%(asctime)s,%(name)s,%(message)s')
defaultLogingLevel = logging.INFO
defaultFileHandler = 'spacefreight.csv'

# Create classes for spacecrafts
class Spacecraft(object):

	# Lukt niet om dit goed over te dragen op de children classes

	def __init__(self, name, spaceleft, kgsleft, density, country):
		self.name = name
		self.spaceleft = spaceleft
		self.kgsleft = kgsleft
		self.density = kgsleft / spaceleft
		self.kgstimesspace = kgsleft * spaceleft
		self.country = country

	def displaySpacecraft(self):
		print ("name: ", self.name, ", Spaceleft: ", self.spaceleft, ", Kgsleft: ", self.kgsleft, ", Densityleft: ", self.density, ", Coutry: ", self.country)

class Cygnus(Spacecraft):

	Cygnuscount = 1

	def __init__(self, name='Cygnus'+ str(Cygnuscount), spaceleft=18.9, kgsleft=2000, density=0, country='USA'):
		Spacecraft.__init__(self, name, spaceleft, kgsleft, density, country)
		Cygnus.Cygnuscount += 1

class VerneATV(Spacecraft):

	VerneATVcount = 1

	def __init__(self, name='VerneATV'+ str(VerneATVcount), spaceleft=13.1, kgsleft=2300, density=0, country='Europe'):
		Spacecraft.__init__(self, name, spaceleft, kgsleft, density, country)
		VerneATV.VerneATVcount += 1

class Progress(Spacecraft):

	Progresscount = 1

	def __init__(self, name='Progress'+ str(Progresscount), spaceleft=7.6, kgsleft=2400, density=0, country='Russia'):
		Spacecraft.__init__(self, name, spaceleft, kgsleft, density, country)
		Progress.Progresscount += 1

class Kounotori(Spacecraft):

	Kounotoricount = 1

	def __init__(self, name='Kounotori'+ str(Kounotoricount), spaceleft=14, kgsleft=5200, density=0, country='Japan'):
	 	Spacecraft.__init__(self, name, spaceleft, kgsleft, density, country)
	 	Kounotori.Kounotoricount += 1

def main():

	# Make spacecrafts
	# heel makkelijk aan te passen hoe veel je van elk soort wil maken 
	Cygnuslist = [Cygnus() for i in range(1)]
	spacecraftsList.extend(Cygnuslist)
	VerneATVlist = [VerneATV() for i in range(1)]
	spacecraftsList.extend(VerneATVlist)
	Progresslist = [Progress() for i in range(1)]
	spacecraftsList.extend(Progresslist)
	Kounotorilist = [Kounotori() for i in range(1)]
	spacecraftsList.extend(Kounotorilist)

	with open('Cargolist1.json') as cargolistFile1:    
	    cargolist1 = json.load(cargolistFile1)

	### SORT CARGOLIST ###
	# Unpack
	cargolist1 = sortmeth.unpack(cargolist1)

	# Weight
	# cargolist1 = sortmeth.sortWeight(cargolist1)

	# Density
	# cargolist1 = sortmeth.sortDensity(cargolist1)
	# for cargo in cargolist1:
	# 	print (cargo["id"])

	# Random
	# cargolist1 = sortmeth.sortRandom(cargolist1)


	# cargoOnlyWeightLeftAircraft(cargolist1)
	cargoMostDensityLeftAircraft(cargolist1)
	# cargoRandom(cargolist1)


	# Display Spacecrafts
	# for Spacecraft in spacecraftsList:
	# 	Spacecraft.displaySpacecraft()

	#inf.infoCargoGround(cargolist1)


	hillClimber(cargolist1, spacecraftsList)

	# 	# Display Spacecrafts
	# for Spacecraft in spacecraftsList:
	# 	Spacecraft.displaySpacecraft()

	# ter vergelijking na hillclimber
	#inf.infoCargoGround(cargolist1)




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
			### Als het goed is opgelost door self.name dynamisch the maken m.b.v. counter###
			# Comment voor iedereen: als we zometeen een lijst hebben met meerdere spacecrafts, dan kun je niet selecteren
			# op naam en al helemaal niet op country (meerdere spacecrafts uit 1 land zometeen) van een bepaald spacecraft, dan moeten we selecteren op id
			cargo['location'] = spacecraft.name

			# update de locatie over van de spacecrafts
			spacecraft.kgsleft -= cargo['kgs']
			spacecraft.spaceleft -= cargo['m3']
			break

def hillClimber (cargolist, spacecraftsList):

	'''
	This Hillclimber Algorithm accepts new situations as better when:
	- There is less m3 or kg left on the ground
	- The trade was between spacecrafts and the spacecraft that innitially had 
	more space (m3) or more kg left, now has even more space or kg left.
	(so that a (larger) package from the ground might fit in this spacecraft now)

	LET OP: Random function generates pseudo-random numbers. Hij is snel en efficient, maar niet goed genoeg voor 
	bijvoorbeeld wachtwoorden
	(https://docs.python.org/2/library/random.html)

	'''
	# Objectives can be m3 or kg in this algorithm
	objective = "m3"
	aantalswaps = 0
	# Setup logger for this algorithm
	logger = logging.getLogger(__name__)
	fileHandler = logging.FileHandler('HillClimberData.csv')
	fileHandler.setLevel(defaultLogingLevel)
	fileHandler.setFormatter(defaultFormatter)
	logger.addHandler(fileHandler)


	# Number of swaps
	# Run hillclimber x times
	for i in range(ITERATIONS):

		# Comment voor Laurens:
		# gebruik == ipv is (zie bijvoorbeeld het bestand 'information.py')
		# is er een reden waarom je daar is gebruikt ipv ==?
		# http://stackoverflow.com/questions/2209755/python-operation-vs-is-not

		# Randomly pick two cargo items from the cargolist
		swapped1 = random.choice(cargolist)
		swapped2 = random.choice(cargolist)

		# Log the swap and the resulting m3 and kg left on the ground
		logger.info('{},{}'.format(i, aantalswaps,))

		# If one of the two is on the ground and the other in the spacecraft
		# Condition 1: swapping reduces objective on the ground (in this case m3)
		# als je 2 en 3 niet snapt: http://stackoverflow.com/questions/7125467/find-object-in-list-that-has-attribute-equal-to-some-value-that-meets-any-condi
		# Condition 2: swapping is possible for kilograms
		# Condition 3: swapping is possible for m3
		# If conditions are met: update spaceleft and kgsleft and swap location of cargo
		if (swapped1['location'] == 'Ground' and swapped2['location'] != 'Ground'):


			if (swapped1[objective] > swapped2[objective]
			and next((x for x in spacecraftsList if x.name == swapped2['location']), None).kgsleft >= swapped1['kgs'] - swapped2['kgs']
			and next((x for x in spacecraftsList if x.name == swapped2['location']), None).spaceleft >= swapped1['m3'] - swapped2['m3']):

				next((x for x in spacecraftsList if x.name == swapped2['location']), None).kgsleft -= swapped1['kgs'] - swapped2['kgs']
				next((x for x in spacecraftsList if x.name == swapped2['location']), None).spaceleft -= swapped1['m3'] - swapped2['m3']
				swapped1['location'], swapped2['location'] = swapped2['location'], swapped1['location']
				aantalswaps += 1




		elif (swapped1['location'] != 'Ground' and swapped2['location'] == 'Ground'):

			if (swapped2[objective] > swapped1[objective]
			and next((x for x in spacecraftsList if x.name == swapped1['location']), None).kgsleft >= swapped2['kgs'] - swapped1['kgs']
			and next((x for x in spacecraftsList if x.name == swapped1['location']), None).spaceleft >= swapped2['m3'] - swapped1['m3']):

				next((x for x in spacecraftsList if x.name == swapped1['location']), None).kgsleft -= swapped2['kgs'] - swapped1['kgs']
				next((x for x in spacecraftsList if x.name == swapped1['location']), None).spaceleft -= swapped2['m3'] - swapped1['m3']
				swapped1['location'], swapped2['location'] = swapped2['location'], swapped1['location']
				aantalswaps += 1


		# # If both are in spacecraft
		# elif (swapped1['location'] != 'Ground' and swapped2['location'] != 'Ground'):

		# 	if (swapped1['kgstimesspace'] > swapped2['kgstimesspace']
		# 	and next((x for x in spacecraftsList if x.name == swapped2['location']), None).kgsleft >= swapped1['kgs'] - swapped2['kgs']
		# 	and next((x for x in spacecraftsList if x.name == swapped2['location']), None).spaceleft >= swapped1['m3'] - swapped2['m3']
		# 	and next((x for x in spacecraftsList if x.name == swapped2['location']), None).kgstimesspace > 
		# 	    next((x for x in spacecraftsList if x.name == swapped1['location']), None).kgstimesspace):
				
		# 		next((x for x in spacecraftsList if x.name == swapped2['location']), None).kgsleft -= swapped1['kgs'] - swapped2['kgs']
		# 		next((x for x in spacecraftsList if x.name == swapped2['location']), None).spaceleft -= swapped1['m3'] - swapped2['m3']
		# 		swapped1['location'], swapped2['location'] = swapped2['location'], swapped1['location']

		# 	if (swapped2['kgstimesspace'] > swapped1['kgstimesspace']
		# 	and next((x for x in spacecraftsList if x.name == swapped1['location']), None).kgsleft >= swapped2['kgs'] - swapped1['kgs']
		# 	and next((x for x in spacecraftsList if x.name == swapped1['location']), None).spaceleft >= swapped2['m3'] - swapped1['m3']
		# 	and next((x for x in spacecraftsList if x.name == swapped1['location']), None).kgstimesspace > 
		# 	    next((x for x in spacecraftsList if x.name == swapped2['location']), None).kgstimesspace):
				
		# 		next((x for x in spacecraftsList if x.name == swapped1['location']), None).kgsleft -= swapped2['kgs'] - swapped1['kgs']
		# 		next((x for x in spacecraftsList if x.name == swapped1['location']), None).spaceleft -= swapped2['m3'] - swapped1['m3']
		# 		swapped1['location'], swapped2['location'] = swapped2['location'], swapped1['location']

		
	print ('aantal swaps', aantalswaps)	
		# 	# Comment voor iedereen: Misschien later nog een all-purpose swap functie maken, we doen dit meerdere keren maar de
		# 	# putcargoinspacecraft function is niet algemeen genoeg voor deze functie

		# Log the configuration of the location of all cargo (comment: daarmee kunnen we vervolgens alles berekenen wat we willen) and which iteration this was

### RUN PROGRAM ###
if __name__ == '__main__':
	main()
	