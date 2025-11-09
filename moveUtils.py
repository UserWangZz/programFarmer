# 关于move的工具包

from builtins import range


def move_ground(action, isWood=False):
	# @brief 遍历整个地图
	# @param action 移动过程中的动作
	# todo:重构思路：后续考虑action为一系列动作集合
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			# 后续考虑action可以为一系列动作
			if isWood:
				# 考虑给树浇水
				if get_entity_type() == Entities.Tree:
					if get_water() < 0.05:
						# 稀缺资源，每次使用一个
						use_item(Items.Water)
						
				action(i,j)
			else:
				action()
			move(North)
		move(East)

def get_shortest_path(cur_x, cur_y, x, y):
	# 获取从当前位置到目标位置的最短路径动作序列
	
	# 参数:
	# cur_x -- 当前位置的x坐标
	# cur_y -- 当前位置的y坐标
	# x -- 目标位置的x坐标
	# y -- 目标位置的y坐标
	
	# 返回:
	# list -- 移动动作序列，元素为'North'、'South'、'West'、'East'
	
	n = get_world_size()
	
	path = []
	
	# 处理水平方向（y轴）的移动，上北下南
	y_diff = y - cur_y
	# 处理垂直方向（x轴）的移动，左西右东
	x_diff = x - cur_x
	
	# 处理垂直方向（x轴）的移动（上下）
	# 计算两种可能的移动距离：直接移动和绕边缘移动
	abs_y_diff = 0
	abs_x_diff = 0
	if x_diff < 0:
		abs_x_diff = -x_diff
	else:
		abs_x_diff = x_diff
	if y_diff < 0:
		abs_y_diff = -y_diff
	else:
		abs_y_diff = y_diff
	wrap_x = n - abs_x_diff   # 绕边缘移动的步数
	wrap_y = n - abs_y_diff
	
	temp_path = []
	
	x_used_temp = False
	y_used_temp = False
	
	if x_diff == 0:
		# 垂直方向无需移动
		pass
	elif abs_x_diff <= wrap_x:
		# 直接移动更短
		if x_diff > 0:
			# 目标在右边，需要向东移动y_diff步
			for i in range(x_diff):
				path.append(East)
		elif x_diff < 0:
			# 目标在左边，需要向西移动(-y_diff)步
			for i in range(-x_diff):
				path.append(West)
	else:
		# 绕边缘移动更短（方向与直接移动相反）
		x_used_temp = True
		if x_diff > 0:
			# 目标在右边，需要向东移动y_diff步
			for i in range(-wrap_x):
				temp_path.append(West)
		elif x_diff < 0:
			# 目标在左边，需要向西移动(-y_diff)步
			for i in range(wrap_x):
				temp_path.append(East)
	
	if y_diff == 0:
		# 垂直方向无需移动
		pass
	elif abs_y_diff <= wrap_y:
		# 直接移动更短
		if y_diff > 0:
			for i in range(y_diff):
				path.append(North)
		elif y_diff < 0:
			for i in range(-y_diff):
				path.append(South)
	else:
		y_used_temp = True
		if y_diff > 0:
			for i in range(-wrap_y):
				temp_path.append(South)
		elif y_diff < 0:
			for i in range(wrap_y):
				temp_path.append(North)
	if x_used_temp and y_used_temp:
		path = temp_path
	elif not x_used_temp and y_used_temp:
		path = path + temp_path
	elif x_used_temp and not y_used_temp:
		path = temp_path + path
	
	return path
	



def moveTo(x, y):
	# @brief 移动一步
	# @param x 目标位置x坐标
	# @param y 目标位置y坐标
	# todo:重构思路：后面地图可能不是长宽相等的矩形
	cur_x = get_pos_x()
	cur_y = get_pos_y()
	path = get_shortest_path(cur_x, cur_y, x, y)
	for direction in path:
		move(direction)


if __name__ == "__main__":
	clear()
	moveTo(0,0)
	moveTo(3,2)