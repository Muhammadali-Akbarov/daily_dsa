/*
	Task:
    	Massiv ichidan bizga kerakli qiymatning
        indexkini(tartib raqamini) qaytaring.
        Agar qidirilyotgan massiv ichida mavjud bo'lmasa
        -1 yoki None qiymatni qaytaring.
    Example:
    	Search(myList,11) -> None
    Tools:
        binary search and linear search
    Hint:
        want -> 10
        value -> 1 3 4 6 7 8 10..
        index -> 0 1 2 3 4 5 6..
        answer -> 6
*/
package intro

import "fmt"

type Searching struct {
	numbers []int
}

func (s *Searching) LinearSearch(numbers []int, input int) int {
	for index, value := range numbers {
		if value == input {
			fmt.Println("index:", index, "value:", value)
		}
	}
}
