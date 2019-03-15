package isogram

import "unicode"

// IsIsogram determines if a word is an isogram
func IsIsogram(word string) bool {
	var seen = make(map[rune]bool)
	for _, r := range word {
		if !unicode.IsLetter(r) {
			continue
		}
		if _, ok := seen[unicode.ToUpper(r)]; ok {
			return false
		}
		seen[unicode.ToUpper(r)] = true
	}
	return true
}
