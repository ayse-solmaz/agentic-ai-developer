package main

import (
	"fmt"
	"os"
	"strconv"

	"example.com/hello/calc"
)

func main() {
	fmt.Println("100C ->", calc.CtoF(100), "F")
	fmt.Println("32F ->", calc.FtoC(32), "C")

	if len(os.Args) != 4 {
		fmt.Println("usage: go run . 10 + 3")
		return
	}

	a, err1 := strconv.Atoi(os.Args[1])
	op := os.Args[2]
	b, err2 := strconv.Atoi(os.Args[3])
	if err1 != nil || err2 != nil {
		fmt.Println("need two integers")
		return
	}

	switch op {
	case "+":
		fmt.Println(a + b)
	case "-":
		fmt.Println(a - b)
	case "*":
		fmt.Println(a * b)
	case "/":
		if b == 0 {
			fmt.Println("division by zero")
			return
		}
		fmt.Println(a / b)
	default:
		fmt.Println("unknown operator")
	}
}
