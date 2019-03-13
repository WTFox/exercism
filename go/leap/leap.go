package leap

func yearDivisibleBy4(year int) bool {
	return year%4 == 0
}

func yearDivisibleBy100(year int) bool {
	return year%100 == 0
}

func yearDivisibleBy400(year int) bool {
	return year%400 == 0
}

// IsLeapYear takes a year and determines if it's a leap year
func IsLeapYear(year int) (result bool) {
	result = false
	if yearDivisibleBy4(year) {
		result = true
		if yearDivisibleBy100(year) && !yearDivisibleBy400(year) {
			result = false
		} else if yearDivisibleBy100(year) {
			result = true
		}
	}
	return
}
