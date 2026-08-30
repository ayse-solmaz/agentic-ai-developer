package main

import "fmt"

func show(p *int) {
	if p == nil {
		fmt.Println("nil, skip")
		return
	}
	fmt.Println("value:", *p)
}

func main() {
	var missing *int
	show(missing)

	n := 7
	show(&n)
}
