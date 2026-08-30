package main

import "fmt"

type User struct {
	Name string
	Age  int
}

func (u User) Adult() bool {
	return u.Age >= 18
}

func main() {
	var z User
	fmt.Println("zero:", z)

	positional := User{"can", 21}
	fmt.Println("positional:", positional)

	keyed := User{Name: "ada", Age: 19}
	fmt.Println("keyed:", keyed)

	p := &User{Name: "efe", Age: 30}
	fmt.Println("pointer:", p.Name, p.Age)

	fmt.Println("ada adult?", keyed.Adult())
	fmt.Println("baby adult?", User{Name: "ali", Age: 3}.Adult())

	fmt.Printf("%%v  %v\n", keyed)
	fmt.Printf("%%+v %+v\n", keyed)
	fmt.Printf("%%#v %#v\n", keyed)
}
func (u User) String() string {
	return fmt.Sprintf("%s (%d)", u.Name, u.Age)
}
