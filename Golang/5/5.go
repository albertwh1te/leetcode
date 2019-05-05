package main

import "fmt"

func longestPalindrome(s string) string {
	// We define dp(i,j)
	// dp(i,j) as following:
	// dp[i,j] = 1  if i ==j
	// =  s[i] == s[j]   if j = i+1
	// =  s[i] == s[j] && dp[i+1][j-1]  if j>i+1
	// dp(0,0) = True

	n := len(s)
	if n <= 1 {
		return s
	}
	start := 0
	end := 0
	maxLength := 0
	dp := make([][]bool, n)
	for i := range dp {
		dp[i] = make([]bool, n)
	}
	for i := range dp {
		dp[i][i] = true
		for j := 0; j < i; j++ {
			dp[j][i] = s[i] == s[j] && (dp[j+1][i-1] || (i == 1+j))
			if dp[j][i] && maxLength < i-j+1 {
				maxLength = i - j + 1
				end = i
				start = j
			}
		}
	}
	return s[start : end+1]
}

func main() {
	t := "babad"
	r := longestPalindrome(t)
	fmt.Println(r)
	fmt.Println(longestPalindrome("ac"))
}
