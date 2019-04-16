package twoSum

func twoSum(nums []int, target int) []int {
	hashtable := make(map[int]int)
	var result []int
	for index, num := range nums {
		hashtable[target-num] = index
	}
	for index, num := range nums {
		if val, ok := hashtable[num]; ok && val != index {
			result = []int{val, index}
		}
	}
	return result
}
