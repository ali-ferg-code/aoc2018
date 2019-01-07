def file_to_squares(filename):

	squares_map = {}
	file = open(filename,"r")
	for line in file:
		to_parse = line.rstrip()
		claim_id = to_parse.split(" @")[0]
		height = int(to_parse.split("x")[1])
		width = int(to_parse.split("x")[0].split(" ")[-1])
		(x1,y1) = to_parse.split("@ ")[1].split(":")[0].split(",")
		rect = (int(x1),int(y1),int(x1)+width,int(y1)+height)
		squares_map[claim_id] = rect
	return squares_map


def parse_file(claims,size):

	fabric = [[0 for x in range(size)] for y in range(size)]

	for claim in claims.values():
		for x in range(claim[0],claim[2]):
			for y in range(claim[1],claim[3]):
				fabric[x][y] +=1
	return fabric


def count_overlaps(matrix):
	overlap_squares = 0
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			if (matrix[i][j] > 1):
				overlap_squares +=1
	return overlap_squares


def no_overlap_id(matrix,claims):
	iterations = 0
	# for each claim
	for claim in claims:
		candidate = True
		rect = claims.get(claim)
		# check each column
		for i in range(rect[0],rect[2]):
			# check each row
			for j in range(rect[1],rect[3]):
				iterations+=1
				# if it contains anything but a 0 disregard that claim
				if(matrix[i][j] != 1):
					candidate = False
					break
			if(not candidate):
				break

		if(candidate):
			return claim


filename = "data/day3.txt"
claims = file_to_squares(filename)
fabric = parse_file(claims,1000)

print(count_overlaps(fabric))
print(no_overlap_id(fabric,claims))
