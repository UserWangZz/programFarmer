from plant_carrot import plant_carrot
from plant_bush import plant_bush
from plant_wood import plant_wood
from moveUtils import *

clear()
do_a_flip()		# do_a_flip理解类似于sleep
while True:
	# 当前逻辑为，如果木头或者干草数量下降到50以下，触发对应刷物品脚本
	# 会将物品刷到1k以上，然后进行刷萝卜
	for i in range(get_world_size()):
		# 判断物品库存是否充足，如果不够充足，会调用对应的刷物品脚本
		numsWood = num_items(Items.Wood)
		numsHay = num_items(Items.Hay)
		numsCarrot = num_items(Items.Carrot)
		for j in range(get_world_size()):
			if numsHay < 50:
				while numsHay < 1000:
					move_ground(plant_bush)
					numsHay = num_items(Items.Hay)
			elif numsWood < 50:
				while numsWood < 1000:
					move_ground(plant_wood, True)
					numsWood = num_items(Items.Wood)
			else:
				plant_carrot()
				moveTo(i,j)