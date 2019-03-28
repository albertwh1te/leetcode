package ReverseLinkedList

type ListNode struct {
	Val  int
	Next *ListNode
}

func reverseList(head *ListNode) *ListNode {
	current := head.Next
	var tmp, previous *ListNode
	for current != nil {
		tmp = current.Next
		current.Next = previous
		previous = current
		current = tmp
	}
	return previous
}
