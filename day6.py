def get_manhattan_distance(a,b):
	return abs((a[0]-b[0])) + abs((a[1]-b[1]))


def closest_node_or_tie_bruteforce(point,nodes):
	
	closest_distance = 100000
	closest_node = -1

	for i in range(len(nodes)):
		distance_to_node = get_manhattan_distance(point,nodes[i])

		if(distance_to_node == closest_distance):
			# found a tie
			closest_node = -1

		if(distance_to_node < closest_distance):
			closest_distance = distance_to_node
			closest_node = i

	return closest_node


def print_field(matrix,minx,miny,maxx,maxy):
	playing_field = 500*[500*[0]]
	for y in range(miny,maxy+1):
		for x in range(minx,maxx+1):
			print(chr((matrix.get((x,y))%50)+97),end="")
		print()	


def combined_distance_to_all_nodes(point,nodes):
	total_distance = 0
	for n in nodes:
		total_distance+=get_manhattan_distance(point,n)
	return total_distance



nodes = []
file = open("data/day6.txt","r")

for line in file:
	(x,y) = line.rstrip().split(",")
	nodes.append((int(x),int(y)))

# get board dimensions (play area)
min_x = 10000
min_y = 10000
max_x = -1
max_y = -1

for i in range(len(nodes)):

	node = nodes[i]

	if(node[0]<min_x):
		min_x = node[0]
	if(node[0]>max_x):
		max_x = node[0]
	if(node[1]<min_y):
		min_y = node[1]
	if(node[1]>max_y):
		max_y = node[1]


#pt1 objects
coordinate_map = {}
territory_counts = dict( [ (i,0) for i in range(len(nodes)) ] )
territory_counts[-1] = 0
invalid_nodes = set()

#pt2 objects
distance_map = {}
potato_area = 0

for y in range(min_y,max_y+1):
	for x in range(min_x,max_x+1):

		#pt1
		closest_node = closest_node_or_tie_bruteforce((x,y),nodes)
		coordinate_map[(x,y)] = closest_node
		territory_counts[closest_node] +=1
		if(x==min_x or x==max_x or y==min_y or y==max_y):
			invalid_nodes.add(closest_node)

		#pt2
		total_distance = combined_distance_to_all_nodes((x,y),nodes)
		if(total_distance < 10000):
			potato_area +=1
		distance_map[(x,y)]  = total_distance


# removing invalid nodes ( any territories that touch the play area border )
for k in invalid_nodes:
    territory_counts.pop(k, None)

print(f"pt1 largest territory: {max(territory_counts.values())}")
print(f"pt2 potato size: {potato_area}")