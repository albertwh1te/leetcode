package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func reverse(head *ListNode) *ListNode {
	var previous, tmp *ListNode
	for head != nil {
		tmp = head.Next
		head.Next = previous
		previous = head
		head = tmp
	}
	return previous
}

func isPalindrome(head *ListNode) bool {
	// 1. find middle,use fast pointer and slow pointer ,fast to end (when fast.next.next is None), slow.next is in the middle
	slow := head
	fast := head
	for fast != nil && fast.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next
	}

	//  if fast != nil , the list had odd length,slow must go next
	if fast != nil {
		slow = slow.Next
	}
	// 2. reverse last half of list
	middle := reverse(slow)

	// 3. compare head to middle, slow to middle if same is true
	for middle != nil {
		if middle.Val != head.Val {
			return false
		}
		middle = middle.Next
		head = head.Next
	}
	return true
}

func main() {
	head := &ListNode{1, nil}
	tail := &ListNode{2, nil}
	head.Next = tail
	fmt.Println(reverse(head).Val)
	fmt.Println(isPalindrome(head))
}
