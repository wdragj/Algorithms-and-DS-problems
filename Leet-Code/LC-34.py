# Medium

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = self.binSearch(nums, target, True)
        end = self.binSearch(nums, target, False)
        
        return [start, end]
    
    # leftS [True/False] if T search left, if F search right
    def binSearch(self, nums, target, leftS):
        l, r = 0, len(nums) - 1
        i = -1 # If target not found, position is -1
        
        while l <= r:
            mid = (l + r) // 2
            
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else: # nums[mid] == target
                i = mid
                if leftS: # Search left
                    r = mid - 1
                else: # Search right
                    l = mid + 1
        
        return i