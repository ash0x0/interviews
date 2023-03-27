func runningSum(nums []int) []int {
	// Objective: for a given array, return an array where each element is the sum of the current and all preceeding elements

	// Calculate a running sum
	// Loop over array
	// Add the current element to the running sum
	// Place in the current index in result arry

	result := make([]int, len(nums))
	sum := 0
	for i := 0; i < len(nums); i++ {
		sum += nums[i]
		result[i] = sum
	}
	return result
} 
