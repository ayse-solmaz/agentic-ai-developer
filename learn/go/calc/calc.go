package calc

// add returns the sum of a and b
func Add(a, b int) int {
	return a + b
}

func Divide(a, b int) (int, bool) {
	if b == 0 {
		return 0, false
	}
	return a / b, true
}

func Split(sum int) (x, y int) {
	x = sum / 2
	y = sum - x
	return
}
func CtoF(c float64) float64 {
	return c*9/5 + 32
}
func FtoC(f float64) float64 {
	return (f - 32) * 5 / 9
}
