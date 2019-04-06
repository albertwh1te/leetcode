package sortedArrayToBST

// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func sortedArrayToBST(nums []int) *TreeNode {
	if len(nums) == 0 {
		return nil
	}
	if len(nums) == 1 {
		return &TreeNode{nums[0], nil, nil}
	}
	index := len(nums) / 2
	root := TreeNode{nums[index], nil, nil}
	root.Left = sortedArrayToBST(nums[0:index])
	root.Right = sortedArrayToBST(nums[index+1:])
	return &root
}
