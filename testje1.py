import json
import os

def itemMergedConstraints(item): return cargo["kgstimesm3"]
def itemValue(item): return item["m3"]
def itemName(item): return item["id"]

exampledict = [{"id":"CL1#1","kgs":22,"m3":11},
			   {"id":"CL1#2","kgs":39,"m3":12},
			   {"id":"CL1#3","kgs":42,"m3":13},
			   {"id":"CL1#4","kgs":29,"m3":14},
			   {"id":"CL1#5","kgs":27,"m3":15},
			   {"id":"CL1#6","kgs":44,"m3":17},
			   {"id":"CL1#7","kgs":27,"m3":18},
			   {"id":"CL1#8","kgs":22,"m3":20},
			   {"id":"CL1#9","kgs":56,"m3":22},
			   {"id":"CL1#10","kgs":31,"m3":22}]

with open('testcargo30.json') as cargolistTest:   
	cargolist = json.load(cargolistTest)

for cargo in cargolist:
	cargo["m3"] *= 100
	cargo["kgstimesm3"] = cargo["m3"] * cargo["kgs"]
	# print cargo

exampleWeightLimit = 120
exampleVolumeLimit = 100
exampleSizeLimit = exampleWeightLimit * exampleVolumeLimit


def pack5(items,sizeLimit):
	P = {}
	for nItems in range(len(items)+1):
		for lim in range(sizeLimit+1):
			if nItems == 0:
				P[nItems,lim] = 0
			elif itemMergedConstraints(items[nItems-1]) > lim:
				P[nItems,lim] = P[nItems-1,lim]
			else:
				P[nItems,lim] = max(P[nItems-1,lim],
				    P[nItems-1,lim-itemMergedConstraints(items[nItems-1])] +
					itemValue(items[nItems-1]))
	
	L = []		
	nItems = len(items)
	lim = sizeLimit
	while nItems > 0:
		if P[nItems,lim] == P[nItems-1,lim]:
			nItems -= 1
		else:
			nItems -= 1
			L.append(itemName(items[nItems]))
			lim -= itemMergedConstraints(items[nItems])

	L.reverse()
	return L

def main():
	print pack5(cargolist,exampleSizeLimit)

if __name__ == '__main__':
  main()