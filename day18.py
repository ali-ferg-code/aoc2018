import sys
import os
import time

def get_adjacent_squares(x,y,verbose=False):

	all_adjacent_squares =""
	if(verbose):
		print(f"{x,y}")

	# top row
	if(y >=1 ):
		all_adjacent_squares+=(land[y-1][max(0,x-1):x+2])
		if(verbose):
			print(land[y-1][max(0,x-1):x+2])

	# middle row
	all_adjacent_squares+=(land[y][max(0,x-1):x+2])
	if(verbose):
		print(land[y][max(0,x-1):x+2])

	#bottom row
	if(y < len(land)-1):
		all_adjacent_squares+=(land[y+1][max(0,x-1):x+2])
		if(verbose):
			print(land[y+1][max(0,x-1):x+2])


	return all_adjacent_squares



def generate(land):
	new_land = []
	for row in range(len(land)):
		new_row = ""
		for col in range(len(land[row])):
			if(land[row][col] == "."):
				#An open acre will become filled with trees if three or more adjacent acres contained trees. Otherwise, nothing happens.
				if(get_adjacent_squares(col,row).count("|")>=3):
					new_row += "|"
				else:
					new_row += "."
			if(land[row][col] == "|"):
				#An acre filled with trees will become a lumberyard if three or more adjacent acres were lumberyards. Otherwise, nothing happens.

				if(get_adjacent_squares(col,row).count("#")>=3):
					new_row += "#"
				else:
					new_row += "|"
			if(land[row][col] == "#"):
				#An acre containing a lumberyard will remain a lumberyard if it was adjacent to at least one other lumberyard and at least one acre containing trees. Otherwise, it becomes open.
				neighbours = get_adjacent_squares(col,row)

				if((neighbours.count("#")>=2) and (neighbours.count("|")>0)):
					new_row += "#"
				else:
					new_row += "."
		new_land.append(new_row)
	return new_land



land = []
with open(sys.argv[1]) as file:
	for l in file:
		land.append(l.strip())


total_generations = int(sys.argv[2])
current_gen = 0
land_scores = {}
gen_scores = {}
while current_gen < total_generations:
	
	# for line in land:
	# 	print(line)

	new_land = generate(land)
	# if(current_gen % 1000 == 0):
	# 	print(f"generation {current_gen}")
	land = new_land
	current_gen+=1
	trees = 0
	lumbers = 0
	for row in land:
		trees += row.count("|")
		lumbers += row.count("#")
	print(current_gen,trees,lumbers,trees * lumbers)
	if(land_scores.get(str(land))):
		loop_start = land_scores.get(str(land))
		loop_end = current_gen
		loop_length = loop_end - loop_start
		print("loop detected")
		print(f"we have found a loop of length {loop_length} starting at {loop_start} and ending at {loop_end}")
		estimated_score = gen_scores[((total_generations-loop_start) % loop_length) + loop_start]
		print(f"pt2 : estimated score at {total_generations} = {estimated_score}")
		break
	else:
		gen_scores[current_gen] = (trees * lumbers)
		land_scores[str(land)] = current_gen


print(f"pt1 : generation {current_gen} = {trees * lumbers}")