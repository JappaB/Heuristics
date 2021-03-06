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
import operator 

# Create classes for spacecrafts
# is dat 'object nodig'? in class Spacecraft (object)
class Spacecraft(object):

	# Lukt niet om dit goed over te dragen op de children classes

	def __init__(self, name, initspace, spaceleft, kgsleft, density, country):
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
locationList = ['Cygnus', 'VerneATV', 'Progress', 'Kounotori', 'Ground']
spacecraftList = []

def main():

	# Import file 
	# LET OP!! (misschien later nog even netjes 
	# met relative paths werken zodat we de cargolist 
	# bestanden in een losse map kunnen zetten en die vervolgens kunnen accessen = netter
	# Voor nu: zorg ervoor dat Cargolist1 in dezelfde file staat als dit python bestand)
	with open('Cargolist1.json') as cargolistFile1:    
	    cargolist1 = json.load(cargolistFile1)

	# Create datastructure
	for cargo in cargolist1:
		cargo['location'] = locationList[4]
		# kg/m2 ratio berekenen voor alles in de cargolist
		cargo['density'] = (cargo['kgs']/cargo['m3'])


	# http://stackoverflow.com/questions/25985566/how-to-sort-a-list-of-objects-based-on-different-object-values-in-python

	# Create spacecrafts

	Cygnus1 = Cygnus()
	VerneATV1 = VerneATV()
	Progress1 = Progress()
	Kounotori1 = Kounotori()

	print(Cygnus1.spaceleft)


	spacecraftList.extend((Cygnus1, VerneATV1, Progress1, Kounotori1))
	print(spacecraftList)

	# lambda http://stackoverflow.com/questions/8966538/syntax-behind-sortedkey-lambda
	spacecraftList.sort(key =lambda x: x.kgsleft, reverse = True)

	print(spacecraftList)

	spacecraftList.sort(key =lambda x: x.spaceleft, reverse = True)

	print(spacecraftList)

	spacecraftList.sort(key =lambda x: x.density, reverse = True)

	print(spacecraftList)

	### SORT CARGOLIST ###
	# Unpack
	#cargolist1 = unpack(cargolist1)

	# Weight
	cargolist1 = sortWeight(cargolist1)

	# Density
	#cargolist1 = sortDensity(cargolist1)

	# Random
	#cargolist1 = sortRandom(cargolist1)


	### ALGORITHMS ###
	# Zet pakketjes in spacecrafts randomly
	#cargoRandom(cargolist1)

	# Zet pakketjes in spacecrafts met most weight left
	#cargoMostWeightLeftAircraft(cargolist1)

	# Zet pakketjes in spacecrafts met most density left
	cargoMostDensityLeftAircraft(cargolist1)

	# Zet pakketjes in spacecraft incl. kijken naar of het precies past
	#fitPrecisely(cargolist1)

	### PRINT INFO ###
	# information on the empty space and weight of the spacecrafts
	#infoCapacity()

	# information on the cargo on the ground
	# depending on which algorithm is used and which cargolist is packed
	infoCargoGround(cargolist1)

	# information on total cargolist
	#infoCargolist(cargolist1)


### FUNCTIONS ###
# Recursively devide the cargo among the different spacecrafts for part B of the asignment
# def cargoRandom (cargolist):

# 	for cargo in cargolist:

# 		listnum = [0, 1, 2, 3]
# 		random.shuffle(listnum)

# 		for elements in listnum:

# 			if countries[elements]['kgsleft'] >= cargo['kgs'] and countries[elements]['spaceleft'] >= cargo['m3']:
# 				cargo['location'] = locationList[elements]
				
# 				# update de locatie over van de aircraft
# 				countries[elements]['kgsleft'] -= cargo['kgs']
# 				countries[elements]['spaceleft'] -= cargo['m3']
# 				countries[elements]['densleft'] = countries[elements]['kgsleft']/countries[elements]['spaceleft']
# 				break

# Set all packages back on ground
def unpack (cargolist):

	for cargo in cargolist:
		cargo['location'] = 'Ground'

	return cargolist

# Sort random
# def sortRandom (cargolist):
	
# 	# create random number generator
# 	shuffledCargolist = cargolist

# 	random.shuffle(shuffledCargolist)

# 	# return random list
# 	return shuffledCargolist

# Sort on density
# def sortDensity (cargolist):
	
# 	# Sort bij density http://stackoverflow.com/questions/72899/how-do-i-sort-a-list-of-dictionaries-by-values-of-the-dictionary-in-python
# 	sortedCargolist = sorted(cargolist, key = lambda k: k['density'], reverse = True)
	
# 	# return sorted list
# 	return sortedCargolist

# Sort on weight
def sortWeight (cargolist):
	
	# Sort by weight http://stackoverflow.com/questions/72899/how-do-i-sort-a-list-of-dictionaries-by-values-of-the-dictionary-in-python
	sortedCargolist = sorted(cargolist, key = lambda k: k['kgs'], reverse = True)
	
	# return sorted list
	return sortedCargolist

# Algorithm to pack cargolist on most density left
def cargoMostDensityLeftAircraft (cargolist):

	# voor elk pakketje in de lijst

	# Sorteer de spacecrafts op density

	for cargo in cargolist:
		# use sort ipv sorted => sorted returns new array http://stackoverflow.com/questions/2338531/python-sorting-a-list-of-objects
		spacecraftList.sort(key =lambda x: x.density, reverse = True)
		
		for spacecraft in spacecrafts:

			# check of er genoeg plek is om het pakketje te plaatsen 
			if densLeft[spacecraft]['kgsleft'] >= cargo['kgs'] and densLeft[spacecraft]['spaceleft'] >= cargo['m3']:

				# zet het pakketje in de minst volle spacecrafts
				cargo['location'] = densLeft[spacecraft]['location']

				# update de locatie over van de spacecrafts
				densLeft[spacecraft]['kgsleft'] -= cargo['kgs']
				densLeft[spacecraft]['spaceleft'] -= cargo['m3']
				densLeft[spacecraft]['densleft'] = densLeft[spacecraft]['kgsleft']/densLeft[spacecraft]['spaceleft']
				break

		# RUILEN HC -> SA

# Check if there is a package that fits precisely in one of the aircrafts
def fitPrecisely (cargolist):
	
	# make array for weight left
	kgsLeft = countries

	# check of er een pakketje is dat precies past in een van de vliegtuigen
	spacecrafts = range(4)
	
	
	for spacecraft in spacecrafts:
		for cargo in cargolist:
			# als er een pakketje is die precies even groot is
			if kgsLeft[spacecraft]['kgsleft'] is cargo['kgs']:
				# zet het pakketje in spacecraft
				cargo['location'] = kgsLeft[spacecraft]['location']

				# update de locatie over van de spacecrafts
				kgsLeft[spacecraft]['kgsleft'] -= cargo['kgs']
				kgsLeft[spacecraft]['spaceleft'] -= cargo['m3']


	# for every package in cargolist
	for cargo in cargolist:

		# sorteer locatielijst op gewichtscapaciteit er over is
		kgsLeft = sorted(kgsLeft, key = lambda k: k['kgsleft'], reverse = True)
		
		spacecrafts = range(4)
		for spacecraft in spacecrafts:

			# check of er genoeg plek is om het pakketje te plaatsen
			if kgsLeft[spacecraft]['kgsleft'] >= cargo['kgs']:

				# zet het pakketje in de minst volle spacecrafts
				cargo['location'] = kgsLeft[spacecraft]['location']

				# update de locatie over van de spacecrafts
				kgsLeft[spacecraft]['kgsleft'] -= cargo['kgs']
				kgsLeft[spacecraft]['spaceleft'] -= cargo['m3']
				break		

	# RUILEN


# Algorithm to pack cargolist on most weight left
def cargoMostWeightLeftAircraft (cargolist):

	# make array for weight left
	kgsLeft = countries

	# for every package in cargolist
	for cargo in cargolist:

		# sorteer locatielijst op gewichtscapaciteit er over is
		kgsLeft = sorted(kgsLeft, key = lambda k: k['kgsleft'], reverse = True)
		
		spacecrafts = range(4)
		for spacecraft in spacecrafts:

			# check of er genoeg plek is om het pakketje te plaatsen
			if kgsLeft[spacecraft]['kgsleft'] >= cargo['kgs']:

				# zet het pakketje in de minst volle spacecrafts
				cargo['location'] = kgsLeft[spacecraft]['location']

				# update de locatie over van de spacecrafts
				kgsLeft[spacecraft]['kgsleft'] -= cargo['kgs']
				kgsLeft[spacecraft]['spaceleft'] -= cargo['m3']
				break		

	# RUILEN


# Print information on the capacity left
def infoCapacity ():

	print("\nBEGIN INFO CAPACITEIT OVER\n")

	for spacecrafts in countries:
		print(spacecrafts['location'])
		print("kgsleft: {}".format(spacecrafts['kgsleft']))
		print("m3left: {}\n".format(spacecrafts['spaceleft']))

	print("EINDE INFO CAPACITEIT OVER\n")

# Print information on packages on the ground
def infoCargoGround (cargolist):

	print("BEGIN INFO CARGO GROND\n")
	
	n_cargo_ground = 0
	kg_cargo_ground = 0
	m3_cargo_ground = 0

	# Check wat er nog over is
	for cargo in cargolist:
		if cargo['location'] is 'Ground':
			n_cargo_ground += 1
			kg_cargo_ground += cargo['kgs']
			m3_cargo_ground += cargo['m3']
			
			print("cargo {}".format(cargo['id']))
			print("kgs: {}".format(cargo['kgs']))
			print("m3: {}\n".format(cargo['m3']))
			
	print("Packages left: {}".format(n_cargo_ground))
	print("Total kgs on ground: {}".format(kg_cargo_ground))
	print("Total m3 on ground: {}\n".format(m3_cargo_ground))
	
	print("EINDE INFO CARGO GROUND\n")

# Print information on all packages
def infoCargolist (cargolist):

	print("BEGIN INFO CARGOLIST\n")

	for cargo in cargolist:
		print("cargo {}".format(cargo['id']))
		print("kgs: {}".format(cargo['kgs']))
		print("m3: {}".format(cargo['m3']))
		print("dens: {}".format(cargo['density']))
		print("location: {}\n".format(cargo['location']))

	print("END INFO CARGOLIST\n")

### RUN PROGRAM ###
if __name__ == '__main__':
	main()
	