package robotname

import (
	"errors"
	"fmt"
	"math/rand"
	"time"
)

var _maxNames = 26 * 26 * 10 * 10 * 10
var namesUsed = make(map[string]int)

type Robot struct {
	name string
}

func (r *Robot) Reset() {
	r.name = ""
	return
}

func (r *Robot) Name() (string, error) {
	if namesUsed == nil {
	}

	if r.name != "" {
		return r.name, nil
	}

	newName, err := r.generateName()
	if err != nil {
		return "", err
	}

	r.name = newName
	return r.name, nil
}

func (r *Robot) generateName() (string, error) {
	if len(namesUsed) == _maxNames {
		return "", errors.New("ew, david")
	}

	var newName string
	for i := 0; i < _maxNames; i++ {
		newName = r.getRandomName()
		_, exists := namesUsed[newName]
		if !exists {
			break
		}
	}

	if newName == "" {
		return "", errors.New("ew")
	}

	namesUsed[newName] = 1
	return newName, nil
}

func (r *Robot) getRandomName() string {
	var letters = []rune("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

	rand.Seed(time.Now().UnixNano())

	return fmt.Sprintf(
		"%s%s%3d",
		string(letters[rand.Intn(len(letters))]),
		string(letters[rand.Intn(len(letters))]),
		rand.Intn(999),
	)
}
