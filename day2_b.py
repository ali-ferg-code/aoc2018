#!/bin/python3
from collections import Counter

words = []
with open('data/day2.txt') as data:
	for line in data:
		words.append( line.rstrip() )

splice_word_matches = {}

for word in words:

	# lets make len(word) checksums for each word
	for char in range(len(word)):
		# cut a letter out of the word
		spliced_word = word[ :char ] + word[ ( char+1 ): ]

		# if we've already seen it then it is a match by 1
		if( splice_word_matches.get( spliced_word ) ):
			# make sure its not self-matching though!
			if( word != splice_word_matches.get( spliced_word ) ):
				print( spliced_word )
		#if its the first time then add the checksum
		else:
			splice_word_matches[ spliced_word ] = word
