import sys

#args {num of generations} {search string}

def print_scores(c,s,scores):
	for i in range(len(scores)):
		if i == c:
			print(f"({scores[i]})",end=" ")
		elif i==s:
			print(f"[{scores[i]}]",end=" ")
		else:
			print(scores[i],end=" ")
	print()


def get_next_ten_scores(generations,scores):

	return scores[generations:generations+10]

generations  = int(sys.argv[1])
test_list = sys.argv[2]

curly_idx = 0
square_idx = 1

scores = "37"

while (len(scores)<generations+11):

	if(scores[-(len(test_list)+1):-1] == test_list ):
		print(len(scores)-(len(test_list)+1))
		exit()
	if(scores[-len(test_list):] == test_list):
		print(len(scores)-len(test_list))
		exit()

	new_recipe_score = int(scores[curly_idx]) + int(scores[square_idx])
	scores += str(new_recipe_score)

	curly_idx = (curly_idx + int(scores[curly_idx]) +1 )% len(scores)
	square_idx = (square_idx + int(scores[square_idx]) +1 )% len(scores)


#print(get_next_ten_scores(generations,scores))
print(f"did not find string, scores is {len(scores)} digits long")

