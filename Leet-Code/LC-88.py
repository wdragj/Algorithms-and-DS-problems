# Easy

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        # Ex) [1,2,3,0,0,0] m = 3 // [2,5,6] n = 3
        
        last = m + n -1 # Last index of nums1 which is m + n - 1
        
        while m > 0 and n > 0:
            if nums1[m - 1] < nums2[n - 1]:
                nums1[last] = nums2[n - 1]
                n -= 1
            else: # nums1[m - 1] >= nums2[n - 1]
                nums1[last] = nums1[m - 1]
                m -= 1
            
            last -= 1
        
        while n > 0:
            nums1[last] = nums2[n - 1]
            last, n = last - 1, n - 1
        
        while m > 0:
            nums1[last] = nums1[m - 1]
            last, m = last - 1, m - 1