package main

import (
	"fmt"
	"sync"
	"sync/atomic"
)

func main() {
	var mu sync.Mutex
	var n int
	var wg sync.WaitGroup
	for i := 0; i < 1000; i++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			mu.Lock()
			n++
			mu.Unlock()
		}()
	}
	wg.Wait()
	fmt.Println("mutex count", n)

	var once sync.Once
	var wg2 sync.WaitGroup
	for i := 0; i < 5; i++ {
		wg2.Add(1)
		go func() {
			defer wg2.Done()
			once.Do(func() {
				fmt.Println("once init")
			})
		}()
	}
	wg2.Wait()

	var a atomic.Int64
	var wg3 sync.WaitGroup
	for i := 0; i < 1000; i++ {
		wg3.Add(1)
		go func() {
			defer wg3.Done()
			a.Add(1)
		}()
	}
	wg3.Wait()
	fmt.Println("atomic count", a.Load())

	fmt.Println("choose: channel for flow; mutex for shared fields")
}
