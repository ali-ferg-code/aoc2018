nodes = {}
visited = []
number_of_dependencies = {}

def get_next(candidate_next_moves,unmet_dependencies):
	list_of_next_possible_moves = list(candidate_next_moves)
	list_of_next_possible_moves.sort()

#	print(f"checking the list {list_of_next_possible_moves}")
#	print(f"to see if any have unmet_dependencies of zero {unmet_dependencies}")
	for i in list_of_next_possible_moves:
		if(unmet_dependencies.get(i) ==0):
			return i

def alphabetic_breadth_first_traverse(nodes,first_moves,unmet_dependencies):
	candidate_next_moves = first_moves
	visited = []

	while len(candidate_next_moves) != 0:

		current_node = get_next(candidate_next_moves,unmet_dependencies)
		candidate_next_moves.remove(current_node)
		visited.append(current_node)
		if(nodes.get(current_node)==None):
			continue
		else:

			for new_node in nodes.get(current_node):
				unmet_dependencies[new_node]-=1
				if(new_node not in visited):
					#print(f"found new node {new_node}")
					candidate_next_moves.add(new_node)
			#print(f"updated candidate_next_moves list: {candidate_next_moves}")
	return visited


with open("data/day7.txt","r") as f:

	from_nodes = set()
	to_nodes = set()

	lines = f.readlines()
	for line in lines:
		this_node = line.split(" ")[1].split(" ")[0]
		next_node = line.split(" ")[7]
		# print(line)
		# print(this_node,next_node)
		if(number_of_dependencies.get(next_node)):
			number_of_dependencies[next_node]+=1
		else:
			number_of_dependencies[next_node]=1

		from_nodes.add(this_node)
		to_nodes.add(next_node)
		if(nodes.get(this_node)):
			nodes[this_node].append(next_node)
		else:
			nodes[this_node] = [next_node]


starting_nodes = from_nodes - to_nodes
for n in starting_nodes:
	number_of_dependencies[n] = 0

order = alphabetic_breadth_first_traverse(nodes,starting_nodes,number_of_dependencies)

print(f"pt1: {"".join(order)}")


