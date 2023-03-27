class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        fst_pntr = 0
        lst_pntr = len(nums) - 1
        for i in range(len(nums)):
            while nums[lst_pntr] == val:
                nums[lst_pntr] = None
                lst_pntr -= 1
            if nums[i] == val:
                nums[i] = nums[lst_pntr]
                nums[lst_pntr] = None
                lst_pntr -= 1
        return len(nums) - nums.count(None) 
