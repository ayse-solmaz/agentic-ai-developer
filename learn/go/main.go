package main

import "fmt"

func main() {
	score :=90

	if score >=90{
		fmt.Println("grade A")
	} else if score >= 70 {
		fmt.Println("grade B")
	} else {
		fmt.Println("grade C")
	}

	// klasik sayaç
	for i :=0;i<3;i++ {
		fmt.Println("n:",i)
	}
	// koşul (başka dillerdeki while)
	n:=3
	for n > 0 {
		fmt.Println("countdown:",n)
		n--
	}

	// range : dilim (slice) üzerinde
	names:=[]string{"can","berke","efe"}
	for i,name:= range names {
		fmt.Println(i,name)
	}
	role := "admin"

	switch role {
	case "admin":
		fmt.Println("full access")
	case "member":
		fmt.Println("read write")
	default:
		fmt.Println("read only")
	}
	
	temp := 18
	switch {
	case temp >= 25:
		fmt.Println("hot")
	case temp >= 15:
		fmt.Println("mild")
	default:
		fmt.Println("cold")
	}
	for i :=0; i<5;i++{
		if i ==2 {
			continue // bu turu atla
		}
		if i== 4 {
			break // döngüyü bitir
		}
		fmt.Println("loop:",i)
	}
	Outer:
	for row :=0;row<3;row++{
		for col :=0;col<3;col++{
			if row == 1 && col ==1 {
				fmt.Println("stop nested at",row,col)
				break Outer
			}
			fmt.Println("cell",row,col)
		}
	}
}
