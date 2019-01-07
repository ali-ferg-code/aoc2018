num_players = 400
last_marble_value = 71864

player_scores = [0] * num_players

def get_next_marble_index(current_index,circle_size):

	if(circle_size<=2):
		return 1
	if(current_index ==circle_size-1):
		return 1
	return (current_index+2)

def get_remove_marble_index(current_index,circle_size):

	if current_index <= 6:
		offset = current_index - 7
		return circle_size + offset

	return current_index-7


def print_circle(l,current_index):
	final_list = str(l[:current_index]) + " " + str(l[current_index]) + " " + str(l[current_index+1:])
	print(final_list)



circle = [0]
current_index = 0
turn = 0

while turn <= last_marble_value:
	player = turn % num_players

	turn +=1
	if(turn % 100000 ==0):
		print(f"turn {turn}")


	if(turn % 23 == 0):

		removeo = get_remove_marble_index(current_index,len(circle))
		current_index = removeo
		player_scores[player]+=turn
		player_scores[player]+=circle[removeo]
		circle.pop(removeo)
		continue

	new_index = get_next_marble_index(current_index,len(circle))
	circle.insert(new_index,turn)
	current_index = new_index
	

print(max(player_scores))
