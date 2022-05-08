# Easy

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Keep moving pointer // Sliding window // Until you find maximum
        # [ -2 1 -3 4 -1 2 1 -5 4 ]
        
        maxNum = nums[0] # Going to iterate through the list, so initially max is whatever is at index 0
        curSum = 0 # Initially 0
        
        for n in nums:
            if curSum < 0: # If whatever came before becomes negative
                curSum = 0 # Reset the sum to 0
            curSum += n # Add the number to sum
            maxNum = max(maxNum, curSum) # Compare the values to the max number and current sum and return whatever is bigger
        
        return maxNum