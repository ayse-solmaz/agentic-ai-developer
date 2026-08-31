package main

import "fmt"

func worker(id int, jobs <-chan int, results chan<- int) {
	for n := range jobs {
		results <- n * n
	}
}

func main() {
	ping := make(chan string)
	go func() {
		ping <- "hello"
	}()
	fmt.Println("unbuffered:", <-ping)

	buf := make(chan int, 2)
	buf <- 1
	buf <- 2
	fmt.Println("buffered:", <-buf, <-buf)

	ch := make(chan int)
	go func() {
		ch <- 10
		ch <- 20
		close(ch)
	}()
	fmt.Print("range:")
	for v := range ch {
		fmt.Print(" ", v)
	}
	fmt.Println()

	jobs := make(chan int, 3)
	results := make(chan int, 3)
	go worker(1, jobs, results)
	jobs <- 2
	jobs <- 3
	jobs <- 4
	close(jobs)
	fmt.Println("squares:", <-results, <-results, <-results)
}
