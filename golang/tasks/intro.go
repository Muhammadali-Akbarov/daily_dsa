/*
Question: 1
    Berilgan:
        Uchta sondan eng kattasini
        topish algorithmini toping.

    Formula:
        a,b,c o'zgaruvchilar yaratamiz
        (a and b) < c yoki (a and c) < b yoki (c and b) < a.

    Yechish:
        If condition bilan.

Question 2:
    1 dan N gacha bo'lgan sonlarni
    ko'paytamsini chiqaring.
*/
package intro

type Numbers struct {
	first, second, third int
}

func (n *Numbers) FindMax() int {
	if n.first > n.second && n.first > n.third {
		return n.first
	}
	if n.second > n.first && n.second > n.third {
		return n.second
	}
	if n.third > n.first && n.third > n.second {
		return n.third
	}
	return 0
}

func factorial(num int) int {
	if num == 1 || num == 0 {
		return num
	}
	return num * factorial(num-1)
}
