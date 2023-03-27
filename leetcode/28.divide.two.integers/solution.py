class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        # GIVEN we have a string
        # WHEN we search for a substring in the striing
        # THEN we get the index of the first occurance index or -1 if the substr doesn't exist

        # loop over haystack
            # loop over needle
        # try to match the needle over the haystack
        # looking for contiguous part of the haystack that matches needles
        # going over haystack + needle together
        # if we find a mismatch, we reset the needle and continue over the haystack

        if len(haystack) < len(needle):
            return -1
        for index in range(len(haystack)):
            start = index
            haystack_itr = start
            needle_itr = 0
            for char in needle:
                if haystack_itr >= len(haystack):
                    return -1
                if char == haystack[haystack_itr]:
                    haystack_itr += 1
                    needle_itr += 1
                else:
                    break
            if needle_itr == len(needle):
                return start
        return -1 
