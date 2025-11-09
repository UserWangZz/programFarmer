# 该函单独种植胡萝卜

from builtins import range
from plant_bush import plant_bush
from plant_wood import plant_wood
from moveUtils import *


def only_plant_carrot():
	# 当前逻辑为，如果木头或者干草数量下降到50以下，触发对应刷物品脚本
	# 会将物品刷到1k以上，然后进行刷萝卜
	for i in range(get_world_size()):
		# 判断物品库存是否充足，如果不够充足，会调用对应的刷物品脚本
		numsWood = num_items(Items.Wood)
		numsHay = num_items(Items.Hay)
		numsCarrot = num_items(Items.Carrot)
		for j in range(get_world_size()):
			if numsHay < 100:
				while numsHay < 3000:
					move_ground(plant_bush)
					numsHay = num_items(Items.Hay)
			elif numsWood < 50:
				while numsWood < 3000:
					move_ground(plant_wood, True)
					numsWood = num_items(Items.Wood)
			else:
				plant_carrot()
				moveTo(i,j)

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