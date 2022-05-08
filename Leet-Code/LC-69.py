# Easy

class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        
        while l <= r:
            mid = (l + r) // 2
            calc = mid * mid
            
            if calc == x:
                return mid
            
            if calc < x:
                l = mid + 1
            else: # calc > x
                r = mid - 1
        
        return r