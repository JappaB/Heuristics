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

	# Lukt niet om dit goed over te dragen op de children classes

	def __init__(self, name, spaceleft, kgsleft, density, country):
		self.name = name
		self.spaceleft = spaceleft
	 	self.kgsleft = kgsleft
	 	self.density = kgsleft / spaceleft
	 	self.country = country

	def displaySpacecraft(self):
	 	print "name: ", self.name, ", Spaceleft: ", self.spaceleft, ", Kgsleft: ", self.kgsleft, ", Densityleft: ", self.density, ", Coutry: ", self.country

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

	Cygnus1 = Cygnus()
	VerneATV1 = VerneATV()
	Progress1 = Progress()
	Kounotori1 = Kounotori()

	Cygnus1.displaySpacecraft()
	VerneATV1.displaySpacecraft()
	Progress1.displaySpacecraft()
	Kounotori1.displaySpacecraft()

	print(Cygnus1.name)


### RUN PROGRAM ###
if __name__ == '__main__':
	main()
	