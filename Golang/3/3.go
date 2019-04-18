package lengthOfLongestSubstring

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func lengthOfLongestSubstring(s string) int {
	result := 0
	left := 0
	right := 0
	stringCode := []rune(s)
	var code [256]int
	for right < len(s) {
		if code[stringCode[right]] != 0 {
			left = max(code[stringCode[right]], left)
		}
		code[stringCode[right]] = right + 1
		right += 1
		result = max(right-left, result)
	}
	return result
}
