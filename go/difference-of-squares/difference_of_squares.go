package diffsquares

// Difference subtractrs SumOfSqureres(num) from SquareOfSum(num)
func Difference(num int) int {
	return SquareOfSum(num) - SumOfSquares(num)
}

// SquareOfSum returns the square of sum(1...Num) inclusive
func SquareOfSum(num int) int {
	ret := num * (num + 1) / 2
	return ret * ret
}

// SumOfSquares returns the sum of squares from 1...Num inclusive
func SumOfSquares(num int) int {
	summedSquares := 0
	for i := 0; i <= num; i++ {
		summedSquares += i * i
	}
	return summedSquares
}
