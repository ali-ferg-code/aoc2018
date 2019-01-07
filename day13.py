import time
import os


def get_vector(direction):
	if(direction == "<"):
		return (-1,0)
	if(direction == "^"):
		return (0,-1)
	if(direction == ">"):
		return (1,0)
	if(direction == "v"):
		return (0,1)

def get_carts(track):

	carts = []
	for row in range(len(track)):
		carts += ([Cart(i,row,j) for i, j in enumerate(track[row]) if j in ['^','v','<','>']])
	return carts

def clean_track(track):
	new_track = []
	for row in track:
		new_row = row.replace("<","-")
		new_row = new_row.replace("^","|") 
		new_row = new_row.replace("v","|")
		new_row = new_row.replace(">","-")
		new_row = new_row.replace("|"," ")
		new_row = new_row.replace("-"," ")
		new_track.append(new_row)
	return new_track


def print_track(track,carts):

	for row in range(len(track)):
		carts_on_row = []
		for c in carts:
			if(c.y == row):
				carts_on_row.append(c)
		if(carts_on_row):
			cart_xs = {}
			for cart in carts_on_row:
				cart_xs[cart.x] = cart
			for col in range(len(track[row])):
				if(cart_xs.get(col)):
					print(cart_xs.get(col).direction,end="")
				else:
					print(track[row][col],end="")
			print()
		else:
			print(track[row])


class Cart:
	def __init__(self,x,y,direction):
		self.x = x 
		self.y = y
		self.direction = direction
		self.vector = get_vector(direction)
		self.intersections_seen = 0
		self.distance_travelled = 0
		self.has_collided = 0


	def __lt__(self, other):
		if(self.y < other.y):
			return True
		elif(self.y > other.y):
			return False
		else:
			return self.x < other.x

	def is_on_intersection(self):
		return (track[self.y][self.x] == "+")

	def is_on_corner(self):
		return ((track[self.y][self.x] == "\\") or (track[self.y][self.x] == "/"))

	def is_on_cart(self,carts):
		for c in carts:
			if(c == self):
				continue
			if(c.x == self.x and c.y == self.y and c.has_collided == 0):
				self.has_collided = 1
				c.has_collided = 1
				return True
		return False

	def intersection_turn(self):

		turn_code = self.intersections_seen%3

		if(turn_code==0):
			if(self.direction == "^"):
				self.direction = "<"
			elif(self.direction == "<"):
				self.direction = "v"
			elif(self.direction == "v"):
				self.direction = ">"
			elif(self.direction == ">"):
				self.direction = "^"
		if(turn_code==2):
			if(self.direction == "^"):
				self.direction = ">"
			elif(self.direction == ">"):
				self.direction = "v"
			elif(self.direction == "v"):
				self.direction = "<"
			elif(self.direction == "<"):
				self.direction = "^"
		self.vector = get_vector(self.direction)
		self.intersections_seen+=1

	def corner_turn(self,corner_char):

		if(corner_char == "/"):
			if(self.direction == "^"):
				self.direction = ">"
			elif(self.direction == "<"):
				self.direction = "v"
			elif(self.direction == ">"):
				self.direction = "^"
			elif(self.direction == "v"):
				self.direction = "<"
		else:
			if(self.direction == "^"):
				self.direction = "<"
			elif(self.direction == "<"):
				self.direction = "^"
			elif(self.direction == ">"):
				self.direction = "v"
			elif(self.direction == "v"):
				self.direction = ">"
			
		self.vector = get_vector(self.direction)

	def move(self,carts):
		self.x = self.x + self.vector[0]
		self.y = self.y + self.vector[1]
		self.land(carts)

	def land(self,carts):
		if(self.is_on_intersection()):
			self.intersection_turn()
		if(self.is_on_corner()):
			self.corner_turn(track[self.y][self.x])
		if(self.is_on_cart(carts)):
			print("Collision")

	def __str___(self):
		return (str(self.x)+ "," + str(self.y) +":"+ self.direction)

	def __repr__(self):
		return (str(self.x)+ "," + str(self.y) +":"+ self.direction)


def get_uncollided_carts(carts):
	return [c for c in carts if c.has_collided==0]


track = []
collisions = 0

with open("data/day13.txt","r") as file:
	for line in file:
		track.append(line.strip("\n"))

carts = get_carts(track)
track = clean_track(track)


print_track(track,carts)
while len(carts) >1 :
	for c in carts:
		if(c.has_collided):
			continue
		c.move(carts)

	carts = get_uncollided_carts(carts)
	carts.sort()

	os.system('cls')
	print_track(track,carts)
	print(len(carts))
	time.sleep(.1)

print_track(track,carts)
print(carts)
