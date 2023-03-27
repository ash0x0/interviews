func runningSum(nums []int) []int {
	// Objective: for a given array, return an array where each element is the sum of index element and all preceeding elements

	// Loop over array
	// Loop over and sum preceeding elements up to and including current element
	// Place the sum in the respective current index in the result array
	if len(nums) < 1 {
		return nums
	}
	var result []int
	for i := 0; i < len(nums); i++ {
		sum := 0
		for j := 0; j <= i; j++ {
			sum = sum + nums[j]
		}
		result = append(result, sum)
	}
	return result
} 
