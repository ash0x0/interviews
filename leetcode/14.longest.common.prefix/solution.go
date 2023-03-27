import "fmt"

func longestCommonPrefix(strs []string) string {
    // Objective: find the longest prefix shared by all array elements
    // Loop over the first element taking increasingly larger prefix each iteration
        // Loop over the remaining elements to see if their prefixes match the selected prefix
            // If one element is found where the prefix doesn't match, return the previous longest prefix
            // If loop falls through, continue on next iteration
    if len(strs) < 1 || len(strs) > 200 {
        return ""
    }
    if len(strs) == 1 {
        return strs[0]
    }
    longestCommon := ""
    for i := 0; i < len(strs[0]); i++ {
        if len(strs[0]) == 0 {
            return longestCommon
        }
        for j := 0; j < len(strs); j++ {
            if len(strs[j]) == 0 || len(strs[j]) < i + 1 {
                return longestCommon
            }
            if strs[j][:i+1] != strs[0][:i+1] {
                return longestCommon
            }
        }
        longestCommon = strs[0][:i+1]
    }
    return longestCommon
} 
