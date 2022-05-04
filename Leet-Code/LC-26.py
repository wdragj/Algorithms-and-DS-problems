# Easy

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        
        # Ex) input [0 0 1 1 1 2 2 3 3 4]
        # Ex) ans [0 1 2 3 4]
        
        for r in range(1, len(nums)):
            if nums[r] != nums[r-1]: # If new value found
                nums[l] = nums[r] # Array at left pointer index is the new value
                l += 1 # Increase left pointer value by 1
        
        return l # return the left pointer value // the number of unique values