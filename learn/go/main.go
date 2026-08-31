package main

import "fmt"

func bumpFirst(s []int) {
	s[0] = 99
}

func main() {
	s := make([]int, 0, 4)
	fmt.Println("len", len(s), "cap", cap(s))
	s = append(s, 1, 2, 3)
	fmt.Println("after append", s, "len", len(s), "cap", cap(s))

	part := s[1:3]
	fmt.Println("slice [1:3]", part)
	part[0] = 8
	fmt.Println("s after part[0]=8", s)

	cp := make([]int, len(s))
	copy(cp, s)
	cp[0] = 7
	fmt.Println("s after copy mutate", s, "cp", cp)

	a := []int{1, 2, 3}
	bumpFirst(a)
	fmt.Println("after bumpFirst", a)

	ages := map[string]int{"ada": 19}
	ages["can"] = 21
	v, ok := ages["efe"]
	fmt.Println("efe", v, ok)
	for k, n := range ages {
		fmt.Println("range", k, n)
	}
}