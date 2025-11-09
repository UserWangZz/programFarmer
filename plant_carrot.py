# 该函单独种植胡萝卜

def only_plant_carrot():
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if can_harvest() and num_items(Items.Wood) > 0 and num_items(Items.Hay) > 0:
				harvest()
				if get_ground_type() == Grounds.Grassland:
					till()
					plant(Entities.Carrot)
				else:
					plant(Entities.Carrot)
				move(North)
		move(East)

def plant_carrot():
	if can_harvest() and num_items(Items.Wood) > 0 and num_items(Items.Hay) > 0:
		harvest()
		if get_ground_type() == Grounds.Grassland:
			till()
			plant(Entities.Carrot)
		else:
			plant(Entities.Carrot)

if __name__ == "__main__":
	clear()
	do_a_flip()
	while True:
		only_plant_carrot()