import sys

# args {input filepath} {number of generations}

def get_points(state,offset):
	num_plants = 0
	for i in range(len(state)):
		if(state[i]=="#"):
			num_plants += i-zero_pot_index

	return(num_plants)

def get_input(filename):

	input = open(filename,"r").readlines()
	state = input[0].split(": ")[1].rstrip()
	rules = {}
	for i in (input[2:]):
		rules[i.split(" =")[0]] = i.split("> ")[1].rstrip()

	return(state,rules)

(state,rules) = get_input(sys.argv[1])

state = "..." + state + "..."
zero_pot_index = 3

for generation in range(int(sys.argv[2])):

	new_state = ""

	wm2 = ".."+state[:3]
	wm1 = "."+state[:4]

	new_state += rules.get(wm2)
	new_state += rules.get(wm1)

	for i in range(2,len(state)-2):

		if(rules.get(state[i-2:i+3])):
			new_state += rules.get(state[i-2:i+3])
		else:
			new_state+= "."

	wp1 = state[-4:]+"."
	wp2 = state[-3:]+".."


	new_state += rules.get(wp1)
	new_state += rules.get(wp2)

	new_state = "." + new_state + ".."

	prev_points = get_points(state,zero_pot_index)
	zero_pot_index +=1
	new_points = get_points(new_state,zero_pot_index)

	state = new_state
	print(f"GEN: {generation+1} PTS: {get_points(state,zero_pot_index)} INC: {new_points-prev_points} @5B: {((50000000000 - generation) * (new_points-prev_points) ) + prev_points}")
