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