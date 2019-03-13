package main

import "fmt"

// Car is a vehicle
type Car struct {
	Color string
	Speed int
}

// Repaint does painting
func (c *Car) Repaint(color string) {
	c.Color = color
}

func main() {
	cars := []Car{
		Car{"Red", 7},
	}

	fmt.Println(cars)
	for i := 1; i <= 10; i++ {
		cars = append(cars, Car{"Blue", i})
	}

	fmt.Println(cars)

	for i := 0; i < len(cars); i++ {
		cars[i].Repaint("Orange")
	}

	fmt.Println(cars)
}
