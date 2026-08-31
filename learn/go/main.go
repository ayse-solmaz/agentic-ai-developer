package main

import (
	"bufio"
	"bytes"
	"errors"
	"fmt"
	"io"
	"os"
	"strings"
)

func readMissing() error {
	_, err := os.ReadFile("no-such-day13.txt")
	if err != nil {
		return fmt.Errorf("read missing: %w", err)
	}
	return nil
}

func main() {
	name := "day13.txt"
	if err := os.WriteFile(name, []byte("hello\nacademy\n"), 0644); err != nil {
		fmt.Println("write:", err)
		return
	}

	raw, err := os.ReadFile(name)
	if err != nil {
		fmt.Println("read:", err)
		return
	}
	fmt.Print("ReadFile:", string(raw))

	f, err := os.Open(name)
	if err != nil {
		fmt.Println("open:", err)
		return
	}
	defer f.Close()

	sc := bufio.NewScanner(f)
	for sc.Scan() {
		fmt.Println("line:", sc.Text())
	}
	if err := sc.Err(); err != nil {
		fmt.Println("scan:", err)
		return
	}

	var buf bytes.Buffer
	w := bufio.NewWriter(&buf)
	if _, err := io.Copy(w, strings.NewReader("via io.Copy")); err != nil {
		fmt.Println("copy:", err)
		return
	}
	w.Flush()
	fmt.Println("copy out:", buf.String())

	err = readMissing()
	fmt.Println("missing wrapped:", err)
	fmt.Println("IsNotExist:", os.IsNotExist(err))
	fmt.Println("errors.Is:", errors.Is(err, os.ErrNotExist))
}