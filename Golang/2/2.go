package addTwoNumbers

/**
 * Definition for singly-linked list.
 */
type ListNode struct {
	Val  int
	Next *ListNode
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	dummy := ListNode{-1, nil}
	current := &dummy
	carry := 0
	for l1 != nil || l2 != nil {
		value := carry
		if l1 != nil {
			value += l1.Val
		}
		if l2 != nil {
			value += l2.Val
		}
		if value >= 10 {
			value = value % 10
			carry = 1
		} else {
			carry = 0
		}
		if l1 != nil {
			l1 = l1.Next
		}
		if l2 != nil {
			l2 = l2.Next
		}
		current.Next = &ListNode{value, nil}
		current = current.Next

	}
	if carry != 0 {
		current.Next = &ListNode{carry, nil}
	}
	return dummy.Next
}
