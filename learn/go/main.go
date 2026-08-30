package main

import "fmt"

type Speaker interface {
	Speak() string
}

type User struct {
	Name string
}

func (u User) Speak() string {
	return u.Name + " says hi"
}

type Bot struct{}

func (b Bot) Speak() string {
	return "beep"
}

func announce(s Speaker) {
	fmt.Println(s.Speak())
}

func main() {
	announce(User{Name: "ada"})
	announce(Bot{})

	var empty Speaker
	fmt.Println("empty iface nil?", empty == nil)

	var p *User
	var wrapped Speaker = p
	fmt.Println("wrapped nil pointer, iface nil?", wrapped == nil)
}
