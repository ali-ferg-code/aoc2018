import re

class Star:
	def __init__(self, initial_position, vector):
		self.initial_position = initial_position
		self.vector = vector
	def point_in_time(self, time):
		x = self.initial_position[0] + (time * self.vector[0])
		y = self.initial_position[1] + (time * self.vector[1])
		return (x,y)


def bounding_box(point_list):
	min_x = 10000
	min_y = 10000
	max_x = -10000
	max_y = -10000
	for p in point_list:
		if(p[0]>max_x):
			max_x = p[0]
		if(p[0]<min_x):
			min_x = p[0]
		if(p[1]>max_y):
			max_y = p[1]
		if(p[1]<min_y):
			min_y = p[1]

	return(min_x,min_y,max_x,max_y)


def box_area(coords):
	return (coords[2]-coords[0]) * (coords[3]-coords[1])


def print_points(bounding_box,stars,time):

	x_points = {}
	y_points = {}

	for s in stars:
		(x,y) = s.point_in_time(time)
		
		if(x_points.get(x)):
			x_points[x].add(s)
		else:
			x_points[x] = set([s])
		if(y_points.get(y)):
			y_points[y].add(s)
		else:
			y_points[y] = set([s])


	for row in range(bounding_box[1],bounding_box[3]+1):
		for col in range(bounding_box[0],bounding_box[2]+1):
			x_stars = x_points.get(col)
			y_stars = y_points.get(row)
			if(x_stars and y_stars):
				if(any(i in x_stars for i in y_stars)):
					print('#', end='')
				else:
					print('.', end='')

			else:
				print('.', end='')

		print()



stars = []

with open('data/day10.txt') as f:
	for line in f:
		nums = re.findall(r"[-\d]+", line)
		position =(int(nums[0]),int(nums[1]))
		velocity = (int(nums[2]),int(nums[3]))
		s = Star(position,velocity)
		stars.append(s)

smallest_box_size = 100000000000
smallest_box_time = 0
smallest_bounding_box = (0,0,0,0)

for t in range(15000):
	time_box = []

	for s in stars:
		time_box.append(s.point_in_time(t))
	box_at_current_time = bounding_box(time_box)
	box_area_at_current_time = box_area(box_at_current_time)
	if(box_area_at_current_time < smallest_box_size):
		smallest_box_time = t
		smallest_box_size = box_area_at_current_time
		smallest_bounding_box = box_at_current_time

print(f"Found box size of {smallest_box_size} at time = {smallest_box_time}, with a bounding box of {smallest_bounding_box}")

print_points(smallest_bounding_box,stars,smallest_box_time)
