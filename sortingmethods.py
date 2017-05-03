# Set all packages back on ground
def unpack (cargolist):

	for cargo in cargolist:
		cargo['density'] = cargo['kgs'] / cargo['m3']
		cargo['kgstimesspace'] = cargo['kgs'] * cargo['m3']
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