package proverb

import "fmt"

// Proverb builds a story around a given slice of nouns
func Proverb(rhyme []string) (output []string) {
	if len(rhyme) == 0 {
		return output
	}
	for i := 0; i < len(rhyme)-1; i++ {
		output = append(output, fmt.Sprintf("For want of a %v the %v was lost.", rhyme[i], rhyme[i+1]))
	}
	return append(output, fmt.Sprintf("And all for the want of a %v.", rhyme[0]))
}
