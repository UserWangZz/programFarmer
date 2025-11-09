# 单纯种植木头
from moveUtils import *

def is_even(x):
	return x % 2 == 0

def only_plant_wood():
	move_ground(plant_wood, True)

def plant_wood(x, y):
	if is_even(x):
		bush_flag = is_even(y)
	else:
		bush_flag = not is_even(y)
	if get_entity_type() == Entities.Grass:
		till()
		if not bush_flag:
			plant(Entities.Bush)
		else:
			plant(Entities.Tree)
	if can_harvest():
		harvest()
		if not bush_flag:
			plant(Entities.Bush)
		else:
			plant(Entities.Tree)

if __name__ == "__main__":
	clear()
	do_a_flip()
	while True:
		only_plant_wood()
