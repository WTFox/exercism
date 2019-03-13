package space

// Planet type to hold Planet name
type Planet string

// getConversion returns the seconds needed to calculate age
func (p *Planet) getConversion() float64 {
	const earthSeconds float64 = 31557600
	conversions := map[Planet]float64{
		"Earth":   earthSeconds,
		"Mercury": earthSeconds * 0.2408467,
		"Venus":   earthSeconds * 0.61519726,
		"Mars":    earthSeconds * 1.8808158,
		"Jupiter": earthSeconds * 11.862615,
		"Saturn":  earthSeconds * 29.447498,
		"Uranus":  earthSeconds * 84.016846,
		"Neptune": earthSeconds * 164.79132,
	}
	return conversions[*p]
}

// Age takes seconds and planet and calculates age
func Age(seconds float64, planet Planet) float64 {
	return seconds / planet.getConversion()
}
