package main

import "fmt"

type User struct {
	Name string
	Age  int
}

func (u User) BirthdayCopy() {
	u.Age++
}

func (u *User) Birthday() {
	u.Age++
}

func (u User) Adult() bool {
	return u.Age >= 18
}

func main() {
	u := User{Name: "ada", Age: 19}

	u.BirthdayCopy()
	fmt.Println("after copy Birthday:", u.Age)

	u.Birthday()
	fmt.Println("after pointer Birthday:", u.Age)

	fmt.Println("adult?", u.Adult())

	p := &u
	p.Birthday()
	fmt.Println("via pointer var:", u.Age)
}