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
USA = {'location': locationList[0],'kg': 2000, 'm3': 18.9}
Europe = {'location': locationList[1],'kg': 2300 ,'m3': 13.1};
Rusia = {'location': locationList[2],'kg': 2400,'m3': 7.6};
Japan = {'location': locationList[3],'kg': 5200,'m3': 14};

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

# Check hoe cargolist eruit ziet
print (cargolist1)

# Sort the cargolist on ???
sortedCargolist1 = cargolist1.sort(key = itemgetter(4))

print(sortedCargolist1)
# Recursively devide the cargo among the different spacecrafts for part B of the asignment
def cargoB (cargolist):

	# Sort bij density http://stackoverflow.com/questions/3121979/how-to-sort-list-tuple-of-lists-tuples
	sortedCargolist1 = sorted(cargolist1, key = lambda tup: tup[1], reverse = True)

	print


	# for cargo in sortedCargolist1:
	# 	if cargo['location'] = locationList[4]:







# # this is the standard boilerplate that calls the main() function
# if __name__ == '__main__':
#     # sys.exit(main(sys.argv)) # used to give a better look to exists
#     main()