package scrabble

import (
	"strings"
)

// Score takes a word and returns the scrabble score
func Score(input string) (totalScore int) {
	letterScoreMap := map[int]string{
		1:  "aeioulnrst",
		2:  "dg",
		3:  "bcmp",
		4:  "fhvwy",
		5:  "k",
		8:  "jx",
		10: "qz",
	}
	word := strings.ToLower(input)
	for _, letter := range strings.Split(word, "") {
		for score, letters := range letterScoreMap {
			if strings.Contains(letters, letter) {
				totalScore += score
			}
		}
	}
	return
}
