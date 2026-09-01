package main

import (
	"fmt"
	"sync"
	"time"
)

func fetch(url string) string {
	time.Sleep(20 * time.Millisecond)
	return "ok:" + url
}

func main() {
	urls := []string{"a.com", "b.com", "c.com"}
	results := make(chan string, len(urls))
	var wg sync.WaitGroup
	for _, u := range urls {
		wg.Add(1)
		go func(u string) {
			defer wg.Done()
			results <- fetch(u)
		}(u)
	}
	go func() {
		wg.Wait()
		close(results)
	}()
	fmt.Print("downloads:")
	for r := range results {
		fmt.Print(" ", r)
	}
	fmt.Println()

	gen := make(chan int)
	go func() {
		for i := 1; i <= 3; i++ {
			gen <- i
		}
		close(gen)
	}()
	sq := make(chan int)
	go func() {
		for n := range gen {
			sq <- n * n
		}
		close(sq)
	}()
	fmt.Print("pipe:")
	for n := range sq {
		fmt.Print(" ", n)
	}
	fmt.Println()

	late := make(chan string, 1)
	go func() {
		time.Sleep(200 * time.Millisecond)
		late <- "body"
	}()
	select {
	case m := <-late:
		fmt.Println("fetch:", m)
	case <-time.After(50 * time.Millisecond):
		fmt.Println("fetch timeout")
	}
}
