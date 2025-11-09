# 交替种植干草和木头

def alternate_cropping_bush_and_grass():
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if can_harvest():
				# 判断是干草还是木头
				if get_entity_type() == Entities.Grass:
					entity_type = Entities.Bush
				else:
					entity_type = Entities.Grass
				harvest()
				plant(entity_type)
				move(North)
		move(East)