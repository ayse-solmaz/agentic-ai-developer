package main

import (
	"fmt"
	"time"
)

func main() {
	fast := make(chan string, 1)
	fast <- "ready"
	slow := make(chan string)
	select {
	case m := <-fast:
		fmt.Println("select:", m)
	case <-slow:
		fmt.Println("select: slow")
	}

	blocked := make(chan int)
	select {
	case <-blocked:
		fmt.Println("got")
	case <-time.After(50 * time.Millisecond):
		fmt.Println("timeout")
	}

	done := make(chan struct{})
	go func() {
		for {
			select {
			case <-done:
				fmt.Println("cancelled")
				return
			default:
				time.Sleep(10 * time.Millisecond)
			}
		}
	}()
	time.Sleep(30 * time.Millisecond)
	close(done)
	time.Sleep(20 * time.Millisecond)

	out := make(chan int, 1)
	dropped := 0
	for i := 0; i < 3; i++ {
		select {
		case out <- i:
		default:
			dropped++
		}
	}
	fmt.Println("dropped", dropped)
}
