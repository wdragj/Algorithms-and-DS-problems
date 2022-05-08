# Easy

class Solution:
    def climbStairs(self, n: int) -> int:
        # Working our way backwards from n to 0
        # It takes 1 way to go from n to n // already at the step
        # It takes 1 way to go from n - 1 to n // 1 step
        # For n - 2, it takes (n - 1) + n
        # Keep shifting one and two's pointer from n-1 and n to the left as n decreases
        
        one, two = 1, 1
        
        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp
            
        return one