package intro

import "testing"

type AddTestData struct {
	num, want int
}

func TestFindMax(t *testing.T) {
	testData := Numbers{
		first: 100, second: 200, third: 300,
	}
	got := testData.FindMax()
	want := 300
	if got != want {
		t.Errorf("FAILED to find max: %v, want %v", got, want)
	}
}

func TestFactarial(t *testing.T) {
	testData := []AddTestData{
		{num: 1, want: 1},
		{num: 2, want: 2},
		{num: 3, want: 6},
		{num: 4, want: 24},
		{num: 5, want: 120},
		{num: 6, want: 720},
		{num: 7, want: 5040},
		{num: 7, want: 5040},
		{num: 8, want: 40320},
		{num: 9, want: 362880},
		{num: 10, want: 3628800},
	}
	for _, item := range testData {
		res := factorial(item.num)
		if res != item.want {
			t.Errorf("Expected %v, got %v", item.want, res)
		}
	}
}
