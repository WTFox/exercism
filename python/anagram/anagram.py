# exercism.io anagram detector
from collections import defaultdict

def detect_anagrams(anagram, anagramList):
	output = []
	mainWordLetterCount = defaultdict(int)
	for letter in anagram:
		mainWordLetterCount[letter.lower()] += 1

	for word in anagramList:
		if word.lower() == anagram.lower():
			continue

		listWordLetterCount = defaultdict(int)
		for letter in word:
			listWordLetterCount[letter.lower()] += 1
		if mainWordLetterCount == listWordLetterCount:
			output.append(word)
			
	return output

if __name__ == '__main__':
	pass
