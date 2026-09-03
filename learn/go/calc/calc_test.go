package calc

import "testing"

func TestAdd(t *testing.T) {
	got := Add(2, 3)
	want := 5
	if got != want {
		t.Fatalf("Add(2, 3) = %d; want %d", got, want)
	}
}

func TestDivide(t *testing.T) {
	got, ok := Divide(10, 2)
	if !ok {
		t.Fatalf("Divide(10, 2) ok = false; want true")
	}
	if got != 5 {
		t.Errorf("Divide(10, 2) = %d; want 5", got)
	}
}

func TestDivideByZero(t *testing.T) {
	got, ok := Divide(10, 0)
	if ok {
		t.Fatalf("Divide(10, 0) ok = true; want false")
	}
	if got != 0 {
		t.Errorf("Divide(10, 0) = %d; want 0", got)
	}
}
