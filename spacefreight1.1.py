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

densLeft = [USA, Europe, Russia, Japan]

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

	
	###ALGORITHMS###
	# Zet pakketjes in spacecrafts randomly
	#cargoRandom(cargolist1)

	# Zet pakketjes in spacecrafts met most weight left
	#cargoMostWeightLeftAircraft(cargolist1)

	# Zet pakketjes in spacecrafts met most density left
	#cargoMostDensityLeftAircraft(cargolist1)


	###INFO###
	# information on the empty space and weight of the spacecrafts
	infocapacity()

	# cargo on the ground depending on which algorithm is used and which cargolist is packed
	cargoground(cargolist1)

# Recursively devide the cargo among the different spacecrafts for part B of the asignment
def cargoRandom (cargolist):

	densLeft = [USA, Europe, Russia, Japan]
	# create random number generator
	shuffledcargolist = cargolist

	random.shuffle(shuffledcargolist)
	
	for cargo in shuffledcargolist:

		listnum = [0, 1, 2, 3]
		random.shuffle(listnum)

		for elements in listnum:

			if densLeft[elements]['kgsleft'] >= cargo['kgs'] and densLeft[elements]['spaceleft'] >= cargo['m3']:
				cargo['location'] = locationList[elements]
				# update de locatie over van de aircraft
				densLeft[elements]['kgsleft'] -= cargo['kgs']
				densLeft[elements]['spaceleft'] -= cargo['m3']
				densLeft[elements]['densleft'] = densLeft[elements]['kgsleft']/densLeft[elements]['spaceleft']
				break



	return shuffledcargolist




	# create random number generator

# Sort on density
def sortDensity (cargolist):
	
	# Sort bij density http://stackoverflow.com/questions/72899/how-do-i-sort-a-list-of-dictionaries-by-values-of-the-dictionary-in-python
	sortedCargolist = sorted(cargolist, key = lambda k: k['density'], reverse = True)
	
	# return sorted list
	return sortedCargolist

# Sort on density
def sortWeight (cargolist):
	
	# Sort by weight http://stackoverflow.com/questions/72899/how-do-i-sort-a-list-of-dictionaries-by-values-of-the-dictionary-in-python
	sortedCargolist = sorted(cargolist, key = lambda k: k['kgs'], reverse = True)
	
	# return sorted list
	return sortedCargolist

# Algoritme om pakketjes in te pakken aan de hand van most density left
def cargoMostDensityLeftAircraft (cargolist):

	densLeft = [USA, Europe, Russia, Japan]
	
	# voor elk pakketje in de lijst
	for cargo in sortDensity(cargolist):

		# sorteer locatielijst op density van de capaciteit die over is
		densLeft = sorted(densLeft, key = lambda k: k['densleft'], reverse = True)
		
		spacecrafts = [0, 1, 2, 3]

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

		
		# for i in range(3):
		# 	if densLeft[i]['kgsleft'] >= cargo['kgs'] and densLeft[i]['spaceleft'] >= cargo['m3']:

		# 		# zet het pakketje in de minst volle spacecrafts
		# 		cargo['location'] = densLeft[i]['location']

		# 		# update de locatie over van de spacecrafts
		# 		densLeft[i]['kgsleft'] -= cargo['kgs']
		# 		densLeft[i]['spaceleft'] -= cargo['m3']
		# 		densLeft[i]['densleft'] = densLeft[i]['kgsleft']/densLeft[i]['spaceleft']

		# 		# ALS IN IFLOOP DAN NAAR NIEUW PAKKET

def infocapacity ():
	# BEGINNEN MET RUILEN, op deze regel?
	print("\nBEGIN INFO CAPACITEIT OVER\n")
	for spacecrafts in densLeft:
		print(spacecrafts['location'])
		print("kgsleft")
		print(spacecrafts['kgsleft'])
		print("spaceleft")
		print(spacecrafts['spaceleft'])
		print("")
	print("EINDE\n")

def cargoground (cargolist):

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
			print("kilo's: {}".format(cargo['kgs']))
			print("kubieke meters {}\n\n".format(cargo['m3']))
			
	# error!! moeten dan gaan ruilen
	print("Pakketjes over: {}".format(n_cargo_ground))
	print("Totaal kilogrammen grond: {}".format(kg_cargo_ground))
	print("Totaal kubieke meters grond: {}\n".format(m3_cargo_ground))
	
	print("EINDE\n")

# Algoritme om pakketjes in te pakken aan de hand van most weight left
def cargoMostWeightLeftAircraft (cargolist):

	# make array for spaceleft
	kgsLeft = [USA, Europe, Russia, Japan]

	# voor elk pakketje in de lijst
	for cargo in sortWeight(cargolist):

		# sorteer locatielijst op gewichtscapaciteit er over is
		kgsLeft = sorted(kgsLeft, key = lambda k: k['kgsleft'], reverse = True)
		
		
		# check of er genoeg plek is om het pakketje te plaatsen 
		if kgsLeft[0]['kgsleft'] >= cargo['kgs']:

			# zet het pakketje in de minst volle spacecrafts
			cargo['location'] = kgsLeft[0]['location']

			# update de locatie over van de spacecrafts
			kgsLeft[0]['kgsleft'] -= cargo['kgs']

		# RUILEN
		else:	
			# Check wat er nog over is
			for cargo in sortWeight(cargolist):
				if cargo['location'] is 'Ground':
					print("cargo {}, kgsleft is {}".format(cargo['id'], cargo['kgs']))
		
			# error!! moeten dan gaan ruilen
			print("Error VAN SANNE")
			return 0

if __name__ == '__main__':
	main()