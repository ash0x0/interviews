func isIsomorphic(s string, t string) bool {
	// Objective
	// determine of two strings are isomorphic, i.e. you can get to t by replacing each character from s with a specific character x

	// Algorithm

	// If strings aren't same length then they're definitely not isomorphic
	if len(s) != len(t) {
		return false
	}

	// Create map of replacement characters x to get from S to T
	charMap := make(map[byte]byte)
	inverseMap := make(map[byte]byte)

	// Loop over S
	for i := 0; i < len(s); i++ {
		// Find the equivalent char in T
		// Insert in map the character x that makes the current character in S -> T
		_, exists := charMap[s[i]]
		if exists && charMap[s[i]] != t[i] {
			return false
		}
		inverseMap[t[i]] = s[i]
		_, exists = inverseMap[t[i]]
		if exists && inverseMap[t[i]] != s[i] {
			return false
		}
		charMap[s[i]] = t[i]
	}

	// If there are repeated values in the map, return false
	if len(charMap) != len(inverseMap) {
		return false
	}

	return true
} 
