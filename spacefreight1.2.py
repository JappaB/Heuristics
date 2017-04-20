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

# Declare list with spacecraft names
Spacecrafts_list = []

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

	# Make spacecrafts
	Cygnus1 = Cygnus()
	Spacecrafts_list.append(Cygnus1)
	VerneATV1 = VerneATV()
	Spacecrafts_list.append(VerneATV1)
	Progress1 = Progress()
	Spacecrafts_list.append(Progress1)
	Kounotori1 = Kounotori()
	Spacecrafts_list.append(Kounotori1)

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
	# cargoMostDensityLeftAircraft(cargolist1)
	cargoRandom(cargolist1)

	inf.infoCargoGround(cargolist1)

	# Display Spacecrafts
	for Spacecraft in Spacecrafts_list:
		Spacecraft.displaySpacecraft()

# Algorithm to pack cargolist on most weight left
def cargoOnlyWeightLeftAircraft (cargolist):

	# for every package in cargolist
	for cargo in cargolist:

		# sorteer locatielijst op gewichtscapaciteit er over is
		Spacecrafts_list.sort(key = lambda k: k.kgsleft, reverse = True)
	
		# if possible, put cargo in spacecraft following a given order
		putCargoinSpacecraftinthefollowingOrder(cargo, Spacecrafts_list)



# Algorithm to pack cargolist on most density left
def cargoMostDensityLeftAircraft (cargolist):

	# voor elk pakketje in de lijst
	for cargo in cargolist:

		# sort list with available spacecrafts on the density of the capacity that is left
		Spacecrafts_list.sort(key = lambda k: k.density, reverse = True)
		
		# if possible, put cargo in spacecraft following a given order
		putCargoinSpacecraftinthefollowingOrder(cargo, Spacecrafts_list)

def cargoRandom (cargolist):

	for cargo in cargolist:

		# sort list with available spacecrafts randomly
		random.shuffle(Spacecrafts_list)

		# if possible, put cargo in spacecraft following a given order
		putCargoinSpacecraftinthefollowingOrder(cargo, Spacecrafts_list)

def putCargoinSpacecraftinthefollowingOrder (cargo, Spacecrafts_list): 

	for spacecraft in Spacecrafts_list:

		# check of er genoeg plek is om het pakketje te plaatsen 
		if spacecraft.kgsleft >= cargo['kgs'] and spacecraft.spaceleft >= cargo['m3']:

			# zet het pakketje in de minst volle spacecrafts
			cargo['location'] = spacecraft.country

			# update de locatie over van de spacecrafts
			spacecraft.kgsleft -= cargo['kgs']
			spacecraft.spaceleft -= cargo['m3']
			break

### RUN PROGRAM ###
if __name__ == '__main__':
	main()
	