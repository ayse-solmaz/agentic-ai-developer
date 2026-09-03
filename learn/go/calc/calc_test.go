package calc

import "testing"

func assertInt(t *testing.T, got, want int) {
	t.Helper()
	if got != want {
		t.Errorf("got %d; want %d", got, want)
	}
}

func assertBool(t *testing.T, got, want bool) {
	t.Helper()
	if got != want {
		t.Errorf("got %v; want %v", got, want)
	}
}

func assertFloat(t *testing.T, got, want float64) {
	t.Helper()
	const eps = 1e-9
	diff := got - want
	if diff < 0 {
		diff = -diff
	}
	if diff > eps {
		t.Errorf("got %v; want %v", got, want)
	}
}

func TestAdd(t *testing.T) {
	tests := []struct {
		name string
		a, b int
		want int
	}{
		{name: "positive", a: 2, b: 3, want: 5},
		{name: "zeros", a: 0, b: 0, want: 0},
		{name: "negative", a: -2, b: 5, want: 3},
		{name: "both_negative", a: -2, b: -3, want: -5},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			assertInt(t, Add(tt.a, tt.b), tt.want)
		})
	}
}

func TestDivide(t *testing.T) {
	tests := []struct {
		name    string
		a, b    int
		want    int
		wantOK  bool
	}{
		{name: "exact", a: 10, b: 2, want: 5, wantOK: true},
		{name: "truncates", a: 7, b: 2, want: 3, wantOK: true},
		{name: "zero_numerator", a: 0, b: 4, want: 0, wantOK: true},
		{name: "negative", a: -10, b: 2, want: -5, wantOK: true},
		{name: "by_zero", a: 10, b: 0, want: 0, wantOK: false},
		{name: "zero_by_zero", a: 0, b: 0, want: 0, wantOK: false},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got, ok := Divide(tt.a, tt.b)
			assertInt(t, got, tt.want)
			assertBool(t, ok, tt.wantOK)
		})
	}
}

func TestSplit(t *testing.T) {
	tests := []struct {
		name    string
		sum     int
		wantX   int
		wantY   int
	}{
		{name: "odd", sum: 7, wantX: 3, wantY: 4},
		{name: "even", sum: 8, wantX: 4, wantY: 4},
		{name: "zero", sum: 0, wantX: 0, wantY: 0},
		{name: "negative", sum: -5, wantX: -2, wantY: -3},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			x, y := Split(tt.sum)
			assertInt(t, x, tt.wantX)
			assertInt(t, y, tt.wantY)
		})
	}
}

func TestCtoF(t *testing.T) {
	tests := []struct {
		name string
		c    float64
		want float64
	}{
		{name: "freezing", c: 0, want: 32},
		{name: "boiling", c: 100, want: 212},
		{name: "negative", c: -40, want: -40},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			assertFloat(t, CtoF(tt.c), tt.want)
		})
	}
}

func TestFtoC(t *testing.T) {
	tests := []struct {
		name string
		f    float64
		want float64
	}{
		{name: "freezing", f: 32, want: 0},
		{name: "boiling", f: 212, want: 100},
		{name: "negative", f: -40, want: -40},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			assertFloat(t, FtoC(tt.f), tt.want)
		})
	}
}