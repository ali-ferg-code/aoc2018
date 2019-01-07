
with open("data/day5.txt") as data:
	full_input=data.read().rstrip()


def reduce(long,remove_char):
	return long.replace((remove_char)+(remove_char.upper()),"").replace((remove_char.upper())+(remove_char),"")

def polymer_reduction(polymer):
	while True:
		len_before = len(polymer)
		for ch in range(ord("a"),ord("z")+1):
			polymer = reduce(polymer,chr(ch))
		if(len(polymer)==len_before):
			return polymer

reduced_length = len(polymer_reduction(full_input))

print(f"pt1: {reduced_length}")

# pt2

min_length = reduced_length

for ch in range(ord("a"),ord("z")+1):
	char_stripped_polymer = full_input.replace(chr(ch),"").replace(chr(ch).upper(),"")
	char_stripped_reduced = polymer_reduction(char_stripped_polymer)
	if(len(char_stripped_reduced) < min_length):
		min_length = len(char_stripped_reduced)

print(f"pt2: {min_length}")

