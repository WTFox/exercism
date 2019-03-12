package hamming

import (
	"errors"
)

var errDifferentLengths = errors.New("inputs are not the same length")

// Distance calculates the hamming distance
func Distance(a, b string) (int, error) {
	if len(a) != len(b) {
		return -1, errDifferentLengths
	}

	var count int
	runeSlice := []rune(b)
	for i, val := range a {
		if val != runeSlice[i] {
			count++
		}
	}
	return count, nil
}
