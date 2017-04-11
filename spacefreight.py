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

def main():

	# Misschien beter om classes te gebruiken in plaats van dicts?
	# Landen als variabele later en naam scpacecraft als naam dictionary
	locationList = ['Cygnus', 'Verne ATV', 'Progress', 'Kounotori', 'Ground']
	USA = {'location': locationList[0],'kg': 2000, 'm3': 18.9, 'spaceleft': 18.9}
	Europe = {'location': locationList[1],'kg': 2300 ,'m3': 13.1, 'spaceleft': 13.1};
	Russia = {'location': locationList[2],'kg': 2400,'m3': 7.6, 'spaceleft': 7.6};
	Japan = {'location': locationList[3],'kg': 5200,'m3': 14, 'spaceleft': 14};

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
		cargo['density'] = (cargo['m3']/cargo['kgs'])

	# Sort the cargolist on density
	sortDensity(cargolist1)

# Recursively devide the cargo among the different spacecrafts for part B of the asignment
def cargoRandom (cargolist1):

	# create random number generator
	print('TODO')

# Recursively devide the cargo among the different spacecrafts for part B of the asignment
def sortDensity (cargolist):
	
	# Sort bij density http://stackoverflow.com/questions/72899/how-do-i-sort-a-list-of-dictionaries-by-values-of-the-dictionary-in-python
	sortedCargolist1 = sorted(cargolist, key = lambda k: k['density'], reverse = True)
	
	for cargo in sortedCargolist1:
		print(cargo)

def cargoLeastFullAircraft (sortedCargolist1):

	# make array for spaceleft
	spaceLeft = {USA, Europe, Russia, Japan}

	# check
	print(spaceLeft)

	# voor elk pakketje in de lijst
	for cargo in sortedCargolist1:

		# sorteer locatielijst op hoeveel plek er over is
		spaceLeft = sorted(spaceLeft, key = lambda k: k['spaceleft'], reverse = True)

		# check of er genoeg plek is om het pakketje te plaatsen 
		if spaceLeft[0]['spaceleft'] < cargo['kgs']:

			# check
			print(spaceLeft)
			print(cargo)

			# error!! moeten dan gaan ruilen
			print("Error")

		# zet het pakketje in de minst volle aircraft
		cargo['location'] = spaceLeft[0]['location']

		# update de locatie over van de aircraft
		spaceLeft[0]['spaceleft'] -= cargo['kgs']

		# check
		print(cargo)

if __name__ == '__main__':
	main()