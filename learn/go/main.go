package main

import (
	"errors"
	"fmt"
)

var ErrEmpty = errors.New("empty name")

type BadAgeError struct {
	Age int
}

func (e BadAgeError) Error() string {
	return fmt.Sprintf("bad age %d", e.Age)
}

func parseUser(name string, age int) (string, error) {
	if name == "" {
		return "", ErrEmpty
	}
	if age < 0 {
		return "", BadAgeError{Age: age}
	}
	return name, nil
}

func load(name string, age int) (string, error) {
	u, err := parseUser(name, age)
	if err != nil {
		return "", fmt.Errorf("load: %w", err)
	}
	return u, nil
}

func main() {
	if _, err := load("", 1); err != nil {
		fmt.Println("empty:", err)
		fmt.Println("is ErrEmpty:", errors.Is(err, ErrEmpty))
	}

	if _, err := load("ada", -3); err != nil {
		fmt.Println("age:", err)
		var bad BadAgeError
		fmt.Println("as BadAge:", errors.As(err, &bad), bad.Age)
	}

	u, err := load("ada", 19)
	if err != nil {
		fmt.Println("unexpected", err)
		return
	}
	fmt.Println("ok", u)
}
