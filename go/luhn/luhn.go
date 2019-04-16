package luhn

import (
	"fmt"
	"strconv"
	"strings"
)

func reverse(s string) (result string) {
	for _, v := range s {
		result = string(v) + result
	}
	return
}

func doubleNum(input int, index int) int {
	if input == 0 {
		return 0
	}
	if index%2 != 0 {
		if input*2 <= 9 {
			return input * 2
		}
		return input*2 - 9
	}
	return input
}

func newInput(input string) []int {
	output := []int{}

	for _, num := range strings.Split(reverse(strings.Replace(input, " ", "", -1)), "") {
		parsedNum, error := strconv.Atoi(num)
		if error == nil {
			output = append(output, parsedNum)
		} else {
			output = append(output, 9)
		}
	}
	return output
}

// Valid takes
func Valid(input string) bool {
	fmt.Println("Input", input)
	if len(input) < 2 {
		fmt.Println(" ")
		return false
	}

	var result int
	sanitizedInput := newInput(input)
	if len(sanitizedInput) < 2 {
		return false
	}
	for idx, num := range sanitizedInput {
		newNum := doubleNum(num, idx)
		result += newNum
	}

	fmt.Println("New input", newInput(input))
	fmt.Println("Result", result)
	fmt.Println(" ")

	if result%10 == 0 {
		return true
	}
	return false
}
