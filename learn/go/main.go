package main

import (
	"fmt"
	"sync"
	"time"
)

func main() {
	var wg sync.WaitGroup
	for i := 1; i <= 3; i++ {
		wg.Add(1)
		go func(n int) {
			defer wg.Done()
			time.Sleep(time.Millisecond * time.Duration(4-n))
			fmt.Println("worker", n)
		}(i)
	}
	wg.Wait()
	fmt.Println("all done")

	var n int
	var wg2 sync.WaitGroup
	for i := 0; i < 1000; i++ {
		wg2.Add(1)
		go func() {
			defer wg2.Done()
			n++
		}()
	}
	wg2.Wait()
	fmt.Println("racy count", n)
}
