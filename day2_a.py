#!/bin/python3
from collections import Counter


doubles = 0
triples = 0

with open('data/day2.txt') as data:
	for line in data:
		c = Counter(line.rstrip())
		counts = c.most_common()
		most_common_size = counts[0][1]

		#if the word has all unique chars, then ignore
		if( most_common_size < 2):
			continue

		#if the word has at least 1 double, score it and ignore it
		if( most_common_size == 2):
			doubles +=1
			continue

		#if the word has at least 1 triple, there are 2 cases:
		#	it may also have a double ( search for at least 1 doubler )
		#	it may have only triples and uniques ( search for )
		if( most_common_size == 3):
			triples+=1
			#search through occurrences for 
			for item in counts:
				if(item[1]==2):
					doubles +=1
					break
				if(item[1]<2):
					break

print(f"there are {doubles} doubles and {triples} triples")
print(f"pt1: {doubles * triples}")
