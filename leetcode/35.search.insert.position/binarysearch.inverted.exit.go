func searchInsert(nums []int, target int) int {
	// Objective
	// Find a target element in array and return its position
	// If target not in array, return where it would be placed if it were inserted in proper order
	// Do it in O(log n)

	// Algorithm
	// Binary Search
	// If target is found then return index
	// If target not found return the current index

	// Set begin index
	start := 0
	// Set end index
	end := len(nums) - 1
	for {
		// If target not found when end index == begin index, return the index
		if start == end {
			if target > nums[start] {
				return start + 1
			} else {
				return start
			}
		}
		// Get middle index
		middle := (start + end) / 2
		// If middle index equals target, return
		// If middle index smaller than target, change begin index to middle index, and end index stays the same
		// If middle index larget than target, change end index to middle index, begin index stays the same
		if nums[middle] == target {
			return middle
		} else if nums[middle] < target {
			start = middle + 1
		} else if nums[middle] > target {
			end = middle
		}
	}
}