# Set all packages back on ground
def unpack (cargolist):

	m3Ground = 0
	kgGround = 0
	cargoOnGround = 0

	for cargo in cargolist:
		cargo['density'] = cargo['kgs'] / cargo['m3']
		cargo['kgstimesspace'] = cargo['kgs'] * cargo['m3']
		cargo['location'] = 'Ground'
		kgGround += cargo['kgs']
		m3Ground += cargo['m3']
		cargoOnGround += 1

	metadata = {"id":"MetaDataOnGround", "kgs":kgGround, "m3":m3Ground, "density":kgGround / m3Ground, "cargoOnGround":cargoOnGround, "location": 'Ground'}
	cargolist.append(metadata)
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