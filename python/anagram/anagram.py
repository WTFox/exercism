# exercism.io anagram detector
from collections import defaultdict


def detect_anagrams(anagram, anagramList):
	output = []

	for word in anagramList:
		if word.lower() == anagram.lower():
			continue

		mainWord = createCounterDict(anagram)
		listWord = createCounterDict(word)
		
		if mainWord == listWord:
			output.append(word)

	return output

def createCounterDict(word):
	wordLetterCount = defaultdict(int)
	for letter in word:
		wordLetterCount[letter.lower()] += 1
	return wordLetterCount


if __name__ == '__main__':
	pass
