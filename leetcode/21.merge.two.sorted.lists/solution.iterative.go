/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
	// Objective
	// Merge two ordered linked lists in the correct order

	// Algorithm
	// Create a new List
	// Iterate over both lists
	// For each iteration, place the lowest element from the two lists in the new list and increment the pointer for that list only

	var mergedList *ListNode
	mergedList = new(ListNode)

	mergedListHead := mergedList

	if list1 == nil {
		return list2
	}
	if list2 == nil {
		return list1
	}
	if list1 == nil && list2 == nil {
		return nil
	}

	for list1 != nil && list2 != nil {
		if list1.Val < list2.Val {
			mergedList.Val = list1.Val
			list1 = list1.Next
		} else {
			mergedList.Val = list2.Val
			list2 = list2.Next
		}
		if list1 != nil && list2 != nil {
			mergedList.Next = new(ListNode)
			mergedList = mergedList.Next
		}
	}

	if list1 == nil && list2 != nil {
		mergedList.Next = list2
	} else if list2 == nil && list1 != nil {
		mergedList.Next = list1
	}

	return mergedListHead
}