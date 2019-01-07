#!/bin/python3
from itertools import cycle


list_of_frequencies = []
seen_frequencies = {}


# reading the file into a list of ints as we will have to do N passes
with open('data/day1.txt') as data:
	for line in data:
		list_of_frequencies.append(int(line.rstrip()))

print(f"pt1 : {sum(list_of_frequencies)}")

# casting to a circular list
frequency_cycle = cycle(list_of_frequencies)

current_frequency = 0
for freq in frequency_cycle:
	current_frequency += freq
	if(seen_frequencies.get(current_frequency)):
		print(f"pt2 : {current_frequency}")
		#once we find our first duplicate, exit
		break
	else:
		seen_frequencies[current_frequency] =1
