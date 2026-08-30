package main

import "fmt"

type User struct {
	Name string
}

func (u User) Role() string {
	return "member"
}

func (u User) Greet() string {
	return "hi " + u.Name
}

type Admin struct {
	User
	Level int
}

func (a Admin) Role() string {
	return "admin"
}

func main() {
	a := Admin{
		User:  User{Name: "ada"},
		Level: 3,
	}

	fmt.Println("promoted Name:", a.Name)
	fmt.Println("promoted Greet:", a.Greet())
	fmt.Println("outer Role:", a.Role())
	fmt.Println("inner Role:", a.User.Role())
	fmt.Println("level:", a.Level)
}
