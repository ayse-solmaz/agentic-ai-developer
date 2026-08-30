package main
import (
	"fmt"
	"example.com/hello/calc"
)

func main() {
	fmt.Println("sum:", calc.Add(2, 3))

	n, ok := calc.Divide(10, 2)
	fmt.Println("10/2:", n, ok)

	n, ok = calc.Divide(10, 0)
	fmt.Println("10/0:", n, ok)

	a, b := calc.Split(7)
	fmt.Println("split:", a, b)
}