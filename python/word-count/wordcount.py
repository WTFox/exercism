# exercism.io word_count
from collections import defaultdict

def word_count(phrase):
	''' Write a program that given a phrase can count the occurrences of each
	word in that phrase.

	For example for the input `"olly olly in come free"

	olly: 2
	in: 1
	come: 1
	free: 1
	'''
	
	output = defaultdict(int)
	for word in phrase.split():
		output[word.lower()] += 1

	return output


if __name__ == "__main__":
    word_count(list(word_count('go Go GO').values()))
