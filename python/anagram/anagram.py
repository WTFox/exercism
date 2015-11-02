# exercism.io anagram detector
from collections import Counter


def detect_anagrams(anagram, anagramList):
	output = []

	for word in anagramList:
		if word.lower() == anagram.lower():
			continue

		mainWord = Counter(anagram.lower())
		listWord = Counter(word.lower())

		if mainWord == listWord:
			output.append(word)

	return output


if __name__ == '__main__':
	pass
