# 单纯种植甘草
from moveUtils import *

def only_plant_bush():
	move_ground(plant_bush)

def plant_bush():
	if get_ground_type() == Grounds.Soil:
		till()
	if can_harvest():
		harvest()

if __name__ == "__main__":
	clear()
	do_a_flip()
	while True:
		only_plant_bush()