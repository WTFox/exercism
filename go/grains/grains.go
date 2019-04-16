package grains

import (
	"errors"
	"math"
)

// Square takes...
func Square(input int) (uint64, error) {
	if input < 1 || input > 64 {
		return 0, errors.New("invalid number")
	}
	return uint64(math.Pow(2, float64(input-1))), nil
}

// Total takes...
func Total() (output uint64) {
	for i := 1; i <= 64; i++ {
		result, _ := Square(i)
		output += result
	}
	return
}
