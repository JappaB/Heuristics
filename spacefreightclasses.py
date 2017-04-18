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

# Create classes for spacecrafts
# is dat 'object nodig'? in class Spacecraft (object)
class Spacecraft(object):

	# 

	# Lukt niet om dit goed over te dragen op de children classes

	# def __init__(self):
	# 	self.density = (self.kgs/self.m3)
	# 	self.cargo = []
	# 	self.spaceleft = self.m3
	# 	self.kgsleft = self.kgs
	# 	self.densityleft = density

	#status
	def status(self):
		print ("This is the: \n")
		print (self.name)
		print("kgsleft")
		print(self.kgsleft)
		print("spaceleft")
		print(self.spaceleft)
		print("densityleft")
		print(self.densityleft)
		print("einde status van")
		print (self.name)

	# Add cargo item to spacecraft
	def append(self, cargo):
		if self.kgsleft >= cargo["kgs"] and self.spaceleft >= cargo["m3"]:
			self.cargo.append(cargo["id"])
			self.kgsleft -= cargo['kgs']
			self.spaceleft -= cargo['m3']
			self.densityleft = (self.kgs/self.m3)
		else:
			print("cargo {} doesn't fit in {}".format(cargo['id'], self.name))

	# Remove cargo item to spacecraft
	def remove(self, cargo):
		# remove removes first  occurrence of element in list (http://stackoverflow.com/questions/2793324/is-there-a-simple-way-to-delete-a-list-element-by-value)
		self.cargo.remove(cargo["id"])
		self.kgs += cargo['kgs']
		self.speaceleft += cargo['m3']
		self.densityleft = (self.kgs/self.m3)

		# cargolist => location = ground


class Cygnus(Spacecraft):

	 #http://stackoverflow.com/questions/5166473/inheritance-and-init-method-in-python
	def __init__(self):
		#Spacecraft.__init__(self, Spacecraft)
		self.name = "Cygnus"
		self.country = "USA"
		self.kgs = 2000
		self.m3 = 18.9
		self.kgsleft = self.kgs
		self.density = (self.kgs/self.m3)
		self.cargo = []
		self.spaceleft = self.m3
		self.kgsleft = self.kgs
		self.densityleft = self.density

class VerneATV(Spacecraft):

	def __init__(self):
		self.name = "Verne ATV"
		self.country = "Europe"
		self.kgs = 2300
		self.m3 = 13.1
		self.density = (self.kgs/self.m3)
		self.cargo = []
		self.spaceleft = self.m3
		self.kgsleft = self.kgs
		self.densityleft = self.density

class Progress(Spacecraft):

	def __init__(self):
		self.name = "Progress"
		self.country = "Russia"
		self.kgs = 2400
		self.m3 = 7.6
		self.density = (self.kgs/self.m3)
		self.cargo = []
		self.spaceleft = self.m3
		self.kgsleft = self.kgs
		self.densityleft = self.density

class Kounotori(Spacecraft):

	def __init__(self):
		self.name = "Kounotori"
		self.country = "Japan"
		self.kgs = 5200
		self.m3 = 14
		self.density = (self.kgs/self.m3)
		self.cargo = []
		self.spaceleft = self.m3
		self.kgsleft = self.kgs
		self.densityleft = self.density


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


	cygnus1 = Cygnus()
	verneATV1 = VerneATV() 
	spacecraftList.append(cygnus1)
	spacecraftList.append(verneATV1)
	print (spacecraftList)
	# print(cygnus1.status())
	# print (type(cargolist1))
	# print (type(cargolist1[0]))
	# cygnus1.append(cargolist1[0])
	# print(cygnus1.status())


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
	infoCapacity()

	# information on the cargo on the ground
	# depending on which algorithm is used and which cargolist is packed
	infoCargoGround(cargolist1)

	# information on total cargolist
	#infoCargolist(cargolist1)


### FUNCTIONS ###
# Recursively devide the cargo among the different spacecrafts for part B of the asignment
def cargoRandom (cargolist):

	for cargo in cargolist:

		listnum = [0, 1, 2, 3]
		random.shuffle(listnum)

		for elements in listnum:

			if countries[elements]['kgsleft'] >= cargo['kgs'] and countries[elements]['spaceleft'] >= cargo['m3']:
				cargo['location'] = locationList[elements]
				
				# update de locatie over van de aircraft
				countries[elements]['kgsleft'] -= cargo['kgs']
				countries[elements]['spaceleft'] -= cargo['m3']
				countries[elements]['densleft'] = countries[elements]['kgsleft']/countries[elements]['spaceleft']
				break

# Set all packages back on ground
def unpack (cargolist):

	for cargo in cargolist:
		cargo['location'] = 'Ground'

	return cargolist

# Sort random
def sortRandom (cargolist):
	
	# create random number generator
	shuffledCargolist = cargolist

	random.shuffle(shuffledCargolist)

	# return random list
	return shuffledCargolist

# Sort on density
def sortDensity (cargolist):
	
	# Sort bij density http://stackoverflow.com/questions/72899/how-do-i-sort-a-list-of-dictionaries-by-values-of-the-dictionary-in-python
	sortedCargolist = sorted(cargolist, key = lambda k: k['density'], reverse = True)
	
	# return sorted list
	return sortedCargolist

# Sort on weight
def sortWeight (cargolist):
	
	# Sort by weight http://stackoverflow.com/questions/72899/how-do-i-sort-a-list-of-dictionaries-by-values-of-the-dictionary-in-python
	sortedCargolist = sorted(cargolist, key = lambda k: k['kgs'], reverse = True)
	
	# return sorted list
	return sortedCargolist

# Algorithm to pack cargolist on most density left
def cargoMostDensityLeftAircraft (cargolist):

	# hou informatie bij van de aircrafts
	densLeft = locationList
	
	# voor elk pakketje in de lijst

	# Sorteer de spacecrafts op density

	for cargo in cargolist:
		#http://stackoverflow.com/questions/2688079/how-to-iterate-over-the-first-n-elements-of-a-list
		for spacecraft in locationList[:4]:
			sorted
			
		# sorteer locatielijst op density van de capaciteit die over is
		densLeft = sorted(densLeft, key = lambda k: k['densleft'], reverse = True)
		
		spacecrafts = range(4)
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

		# RUILEN

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
	