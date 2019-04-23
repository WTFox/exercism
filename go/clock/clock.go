package clock

import "fmt"

// A huge thanks to Cody for the solution!

// Clock struct
type Clock struct {
	hours, minutes int
}

// recalibrateValues normalizes h, m values
func (c *Clock) recalibrateValues() {
	for ; c.minutes > 59; c.hours++ {
		c.minutes -= 60
	}

	for ; c.minutes < 0; c.hours-- {
		c.minutes += 60
	}

	c.hours = c.hours % 24
	if c.hours < 0 {
		c.hours += 24
	}
	return
}

// String returns the string representation of c (Clock)
func (c Clock) String() string {
	return fmt.Sprintf("%02d:%02d", c.hours, c.minutes)
}

// Add minutes (m) to a Clock (c)
func (c Clock) Add(m int) Clock {
	c.minutes += m
	c.recalibrateValues()
	return c
}

// Subtract minutes (m) from a Clock (c)
func (c Clock) Subtract(m int) Clock {
	c.minutes -= m
	c.recalibrateValues()
	return c
}

// New instantiates a new Clock
func New(h, m int) Clock {
	c := Clock{h, m}
	c.recalibrateValues()
	return c
}
