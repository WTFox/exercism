package isogram

import "strings"

func sliceContains(collection []string, value string) bool {
	for _, val := range collection {
		if val == value {
			return true
		}
	}
	return false
}

// IsIsogram determines if a word is an isogram
func IsIsogram(word string) bool {
	var seen []string
	for _, letter := range strings.Split(strings.ToLower(word), "") {
		if strings.Contains("- ", letter) {
			continue
		}
		if sliceContains(seen, letter) {
			return false
		}
		seen = append(seen, letter)
	}
	return true
}
