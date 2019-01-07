

def next_element():
	global cursor
	cursor+=1
	return tree[cursor-1]


def parse_tree():
	global cursor
	num_children = next_element()
	num_metadata = next_element()

	child_nodes = []
	metadata_nodes  = []

	for child in range(num_children):
		child_nodes.append(parse_tree())
	for meta in range(num_metadata):
		metadata_nodes.append(next_element())
	return (child_nodes,metadata_nodes)

def sum_children(children,metadata):
	print(f"summing for {children},{metadata}")
	total = 0
	for i in metadata:
		total +=i
	for c in children:
		total += sum_children(c[0],c[1])
	print(f"returning {total}")
	return total

def value(children,metadata):
	print(f"getting value for {children} , {metadata}")
	if(not children):
		print(f"have no children so returning {sum(metadata)}")
		return sum(metadata)
	else:
		total = 0 
		for c in metadata:
			print(f"checking if child {c} can be added")
			if(c > 0 and c <= len(children)):
				print(f"recursing with {c}")
				total += value(children[c-1][0],children[c-1][1])
			else:
				print("(it can't)")
		return total


with open('data/day8.txt') as f:
    tree = [int(x) for x in next(f).split()] # read first line


cursor = 0

top_level = parse_tree()
print(sum_children(top_level[0],top_level[1]))
print(value(top_level[0],top_level[1]))