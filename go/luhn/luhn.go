package luhn

import (
	"strconv"
	"strings"
)

func doubleNum(num int) int {
	if num*2 <= 9 {
		return num * 2
	}
	return num*2 - 9
}

func sanitizeInput(input string) (output []int, offset int) {
	input = strings.Replace(input, " ", "", -1)
	for _, num := range strings.Split(input, "") {
		parsedNum, error := strconv.Atoi(num)
		if error != nil {
			offset++
			continue
		}
		output = append(output, parsedNum)
	}
	return
}

// Valid takes a string and returns true if it's valid according
// to the Luhn algorithm
func Valid(input string) bool {
	sanitizedInput, offset := sanitizeInput(input)

	if len(sanitizedInput) < 2 {
		return false
	}

	var greedyResult int
	for idx, num := range sanitizedInput {
		if len(sanitizedInput)%2 != 0 {
			idx++
		}
		if idx%2+offset == 0 {
			greedyResult += doubleNum(num)
		} else {
			greedyResult += num
		}
	}
	return greedyResult%10 == 0
}
