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

# Misschien beter om classes te gebruiken in plaats van dicts?
# Landen als variabele later en naam scpacecraft als naam dictionary
locationList = ['Cygnus', 'Verne ATV', 'Progress', 'Kounotori', 'Ground']
USA = {'location': locationList[0],'kgs': 2000, 'm3': 18.9, 'density': 2000/18.9, 'spaceleft': 18.9, 'kgsleft': 2000, 'densleft': 2000/18.9}
Europe = {'location': locationList[1],'kgs': 2300 ,'m3': 13.1, 'density': 2300/13.1, 'spaceleft': 13.1, 'kgsleft': 2300, 'densleft': 2300/13.1};
Russia = {'location': locationList[2],'kgs': 2400,'m3': 7.6, 'density': 2400/7.6, 'spaceleft': 7.6, 'kgsleft': 2400, 'densleft': 2400/7.6};
Japan = {'location': locationList[3],'kgs': 5200,'m3': 14, 'density': 5200/14, 'spaceleft': 14, 'kgsleft': 5200, 'densleft': 5200/14};

countries = [USA, Europe, Russia, Japan]

def main():

	### IMPORT FILES ###
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
	cargoMostWeightLeftAircraft(cargolist1)

	# Zet pakketjes in spacecrafts met most density left
	#cargoMostDensityLeftAircraft(cargolist1)

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
	densLeft = countries
	
	# voor elk pakketje in de lijst
	for cargo in cargolist:

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