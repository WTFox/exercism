package grains

import (
	"errors"
	"math"
)

// Square takes
func Square(input int) (uint64, error) {
	if input < 1 || input > 64 {
		return 0, errors.New("invalid number")
	}
	return uint64(math.Pow(2, float64(input-1))), nil
}

// Total takes
func Total() uint64 {
	output, _ := Square(65)
	return output
}
