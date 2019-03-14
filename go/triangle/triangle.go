package triangle

import "math"

// Kind determines triangle type
type Kind int

// Constants for triangle Kinds
const (
	NaT = iota
	Equ
	Iso
	Sca
)

func isInvalidTriangle(a, b, c float64) bool {
	// A valid triangle,
	// 1) all sides have to be of length > 0,
	for _, val := range []float64{a, b, c} {
		if math.IsInf(val, 0) || math.IsNaN(val) || val <= 0 {
			return true
		}
	}
	// 2) the sum of the lengths of any two sides must be greater than
	// 	  or equal to the length of the third side
	return a+b < c || c+b < a || a+c < b
}

func isEquilateral(a, b, c float64) bool {
	// An Equilateral triangle has all three sides the same length.
	return a == b && b == c
}

func isIsosceles(a, b, c float64) bool {
	// An Isosceles triangle has at least two sides the same length.
	return a == b || b == c || c == a
}

func isScalene(a, b, c float64) bool {
	// A Scalene triangle has all sides of different lengths.
	// So, not an equilateral or Isosceles triangle.
	return !isEquilateral(a, b, c) && !isIsosceles(a, b, c)
}

// KindFromSides takes 3 sides and returns the type of Triangle they
// represent.
func KindFromSides(a, b, c float64) (k Kind) {
	switch {
	case isInvalidTriangle(a, b, c):
		k = NaT
	case isEquilateral(a, b, c):
		k = Equ
	case isScalene(a, b, c):
		k = Sca
	case isIsosceles(a, b, c):
		k = Iso
	}
	return
}
