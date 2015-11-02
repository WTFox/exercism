# exercism.io anagram detector


def detect_anagrams(anagram, anagramList):
	return [word for word in anagramList 
				if not word.lower() == anagram.lower() 
					and sorted(word.lower()) == sorted(anagram.lower())]


if __name__ == '__main__':
	pass
