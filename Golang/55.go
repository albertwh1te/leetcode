package main

func canJump(nums []int) bool {
	mostFar := nums[0]
	for index := 1; index < len(nums)-1; index++ {
		if nums[index]+index > mostFar && mostFar >= index {
			mostFar = nums[index] + index
		}
	}
	return mostFar >= len(nums)-1
}
