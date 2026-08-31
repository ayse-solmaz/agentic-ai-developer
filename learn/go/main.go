package main

import (
	"encoding/json"
	"errors"
	"fmt"
	"os"
	"strings"
)

type Config struct {
	Name string `json:"name"`
}

func loadConfig(path string) (Config, error) {
	raw, err := os.ReadFile(path)
	if err != nil {
		return Config{}, fmt.Errorf("config: %w", err)
	}
	var c Config
	if err := json.Unmarshal(raw, &c); err != nil {
		return Config{}, fmt.Errorf("config json: %w", err)
	}
	if strings.TrimSpace(c.Name) == "" {
		return Config{}, errors.New("config: name required")
	}
	return c, nil
}

func countWords(path string) (map[string]int, error) {
	raw, err := os.ReadFile(path)
	if err != nil {
		return nil, fmt.Errorf("data: %w", err)
	}
	freq := map[string]int{}
	for _, w := range strings.Fields(string(raw)) {
		freq[w]++
	}
	return freq, nil
}

type Summary struct {
	Name  string         `json:"name"`
	Words map[string]int `json:"words"`
}

func main() {
	if err := os.WriteFile("day15-config.json", []byte(`{"name":"lab"}`), 0644); err != nil {
		fmt.Println(err)
		return
	}
	if err := os.WriteFile("day15-data.txt", []byte("go go json go"), 0644); err != nil {
		fmt.Println(err)
		return
	}

	cfg, err := loadConfig("day15-config.json")
	if err != nil {
		fmt.Println("load:", err)
		return
	}
	freq, err := countWords("day15-data.txt")
	if err != nil {
		fmt.Println("count:", err)
		return
	}
	out, err := json.Marshal(Summary{Name: cfg.Name, Words: freq})
	if err != nil {
		fmt.Println("summary:", err)
		return
	}
	if err := os.WriteFile("day15-summary.json", out, 0644); err != nil {
		fmt.Println("write summary:", err)
		return
	}
	fmt.Println("summary:", string(out))

	_, err = loadConfig("no-such-config.json")
	fmt.Println("missing:", err != nil, errors.Is(err, os.ErrNotExist))

	if err := os.WriteFile("day15-bad.json", []byte(`{not json`), 0644); err != nil {
		fmt.Println(err)
		return
	}
	_, err = loadConfig("day15-bad.json")
	fmt.Println("malformed:", err != nil)

	if err := os.WriteFile("day15-empty.json", []byte(`{"name":""}`), 0644); err != nil {
		fmt.Println(err)
		return
	}
	_, err = loadConfig("day15-empty.json")
	fmt.Println("empty name:", err != nil)
}
