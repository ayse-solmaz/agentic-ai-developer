package main

import (
	"fmt"
	"math"
)

type Shape interface {
	Area() float64
	Perimeter() float64
}
type Circle struct {
	R float64
}

func (c Circle) Area() float64 {
	return math.Pi * c.R * c.R
}
func (c Circle) Perimeter() float64 {
	return 2 * math.Pi * c.R
}

type Rectangle struct {
	W, H float64
}

func (r Rectangle) Area() float64 {
	return r.W * r.H
}
func (r Rectangle) Perimeter() float64 {
	return 2 * (r.W + r.H)
}
func printShape(name string, s Shape) {
	fmt.Println(name, "area", s.Area(), "peri", s.Perimeter())
}

type Logger interface {
	Log(msg string)
}
type ConsoleLogger struct{}

func (ConsoleLogger) Log(msg string) {
	fmt.Println("log:", msg)
}

type NoopLogger struct{}

func (NoopLogger) Log(string) {}

func main() {
	c := Circle{R: 1}
	rect := Rectangle{W: 2, H: 3}
	printShape("circle", c)
	printShape("rect", rect)

	wantArea := 6.0
	gotArea := rect.Area()
	fmt.Println("rect area table", "want", wantArea, "got", gotArea, "ok", gotArea == wantArea)

	var logs Logger = ConsoleLogger{}
	logs.Log("shapes done")
	logs = NoopLogger{}
	logs.Log("you should not see this")
}
