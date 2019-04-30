package main

import (
	"fmt"
)

func min(x, y int) int {
	if x > y {
		return y
	}
	return x
}

func findKth(nums1, nums2 []int, k int) int {
	m := len(nums1)
	n := len(nums2)
	// we assume that len(nums2) is greater than len(nums1)
	if m > n {
		return findKth(nums2, nums1, k)
	}
	if m == 0 {
		return nums2[k-1]
	}
	if k == 1 {
		return min(nums2[0], nums1[0])
	}
	p1 := min(k>>1, m)
	p2 := k - p1
	if nums1[p1-1] == nums2[p2-1] {
		return nums1[p1-1]
	} else if nums1[p1-1] < nums2[p2-1] {
		return findKth(nums1[p1:], nums2, p2)
	}
	return findKth(nums1, nums2[p2:], p1)
}

func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
	m := len(nums1)
	n := len(nums2)
	// even number
	if (m+n)%2 == 0 {
		return float64(findKth(nums1, nums2, ((m+n)>>1)+1)+findKth(nums1, nums2, (m+n)>>1)) * 0.5
	}
	return float64(findKth(nums1, nums2, (m+n)>>1+1))
}

func main() {
	fmt.Printf("median of [1,3] and [2] is %v \n", findMedianSortedArrays([]int{1, 3}, []int{2}))
	fmt.Printf("median of [1,2] and [3,4] is %v \n", findMedianSortedArrays([]int{1, 2}, []int{3, 4}))
	fmt.Printf("median of [] and [1] is %v \n", findMedianSortedArrays([]int{}, []int{1}))
}
