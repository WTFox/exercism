package letter

// FreqMap records the frequency of each rune in a given text.
type FreqMap map[rune]int

// Frequency counts the frequency of each rune in a given text and returns this
// data as a FreqMap.
func Frequency(s string) FreqMap {
	m := FreqMap{}
	for _, r := range s {
		m[r]++
	}
	return m
}

// ConcurrentFrequency does a thing.
func ConcurrentFrequency(list []string) FreqMap {
	ch := make(chan FreqMap, len(list))
	for _, text := range list {
		go func(text string) {
			ch <- Frequency(text)
		}(text)
	}

	m := FreqMap{}
	for range list {
		for letter, freq := range <-ch {
			m[letter] += freq
		}
	}

	return m
}
