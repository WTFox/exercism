package raindrops

import "fmt"

// Convert does plinging, planging, and plongning
func Convert(num int) (output string) {
	sounds := []string{"Pling", "Plang", "Plong"}
	for idx, value := range []int{3, 5, 7} {
		if num%value == 0 {
			output += sounds[idx]
		}
	}
	if len(output) == 0 {
		output = fmt.Sprintf("%v", num)
	}
	return
}
