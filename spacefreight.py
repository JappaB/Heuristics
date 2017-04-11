'''
Heuristieken blok 5 2016-2017
Space Freight opdracht B

Jasper Bakker (10260250)
Sanne Berendschot (10269290)
Laurens vd Ziel (10653384)

'''

# Import packages
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

	# Sort the cargolist on density
	# sortedCargolist1 = sortDensity(cargolist1)

	# Sort the cargolist on weight
	sortedCargolist1 = sortWeight(cargolist1)

	# Zet pakketjes in aircrafts met most weight left
	#cargoMostWeightLeftAircraft(sortedCargolist1)

	# Zet pakketjes in aircrafts met most density left
	cargoMostDensityLeftAircraft(sortedCargolist1)

# Recursively devide the cargo among the different spacecrafts for part B of the asignment
def cargoRandom (cargolist1):

	# create random number generator
	print('TODO')

# Sort on density
def sortDensity (cargolist):
	
	# Sort bij density http://stackoverflow.com/questions/72899/how-do-i-sort-a-list-of-dictionaries-by-values-of-the-dictionary-in-python
	sortedCargolist1 = sorted(cargolist, key = lambda k: k['density'], reverse = True)
	
	# return sorted list
	return sortedCargolist1

# Sort on density
def sortWeight (cargolist):
	
	# Sort by weight http://stackoverflow.com/questions/72899/how-do-i-sort-a-list-of-dictionaries-by-values-of-the-dictionary-in-python
	sortedCargolist1 = sorted(cargolist, key = lambda k: k['kgs'], reverse = True)
	
	# return sorted list
	return sortedCargolist1

# Algoritme om pakketjes in te pakken aan de hand van most density left
def cargoMostDensityLeftAircraft (sortedCargolist1):

	# make array for spaceleft
	densLeft = [USA, Europe, Russia, Japan]

	n = 0
	# voor elk pakketje in de lijst
	for cargo in sortedCargolist1:

		# sorteer locatielijst op hoeveel plek er over is
		densLeft = sorted(densLeft, key = lambda k: k['densleft'], reverse = True)

		for spacecraft in densLeft:
			print spacecraft['densleft']
		return 0
		#print("")
		#print("densleft is")
		#print densLeft[0]['densleft']
		#print("cargo {} densleft is".format(cargo['id']))
		#print cargo['kgs']

		# check of er genoeg plek is om het pakketje te plaatsen 
		if densLeft[0]['kgsleft'] < cargo['kgs'] or densLeft[0]['spaceleft'] < cargo['m3']:

			print n
			# check of het klopt
			# for spacecraft in densLeft:
			# 	print spacecraft['densleft']
			# print("")
			# print(cargo['density'])

			i = 0
			# Check wat er nog over is
			for cargo in sortedCargolist1:
				if cargo['location'] is 'Ground':
					i += 1
					# print("cargo {} densleft is".format(cargo['id']))
					# print(cargo['kgs'])
					# print(cargo['m3'])
			# error!! moeten dan gaan ruilen
			print i
			print("Error")
			return 0

		# zet het pakketje in de minst volle aircraft
		cargo['location'] = densLeft[0]['location']

		# update de locatie over van de aircraft
		densLeft[0]['kgsleft'] -= cargo['kgs']
		densLeft[0]['spaceleft'] -= cargo['m3']
		densLeft[0]['densleft'] = densLeft[0]['kgsleft']/densLeft[0]['spaceleft']

		n += 1
		# check
		#print(cargo)

# Algoritme om pakketjes in te pakken aan de hand van most weight left
def cargoMostWeightLeftAircraft (sortedCargolist1):

	# make array for spaceleft
	kgsLeft = [USA, Europe, Russia, Japan]

	# voor elk pakketje in de lijst
	for cargo in sortedCargolist1:

		# sorteer locatielijst op hoeveel plek er over is
		kgsLeft = sorted(kgsLeft, key = lambda k: k['kgsleft'], reverse = True)
		
		# check of er genoeg plek is om het pakketje te plaatsen 
		if kgsLeft[0]['kgsleft'] < cargo['kgs']:

			# Check wat er nog over is
			for cargo in sortedCargolist1:
				if cargo['location'] is 'Ground':
					print("cargo {} kgsleft is".format(cargo['id']))
					print(cargo['kgs'])
		
			# error!! moeten dan gaan ruilen
			print("Error")
			return 0

		# zet het pakketje in de minst volle aircraft
		cargo['location'] = kgsLeft[0]['location']

		# update de locatie over van de aircraft
		kgsLeft[0]['kgsleft'] -= cargo['kgs']

if __name__ == '__main__':
	main()