# Easy

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False # If x is ever negative, it can't be a palindrone, return False
        
        div = 1 # Divider
        while x >= 10 * div: # While x is greater than or equal to 10 * divider
            div *= 10 # Divider will increase 1 digit // Ex) 10 => 100 => 1000
        
        while x: # While x is not 0
            right = x % 10 # The right digit is x mod 10 // To get the 1st digit's place
            left = x // div # Left is x floor-divide by the divider
            
            if left != right: return False # If ever the left and right isn't same, return False
            
            x = (x % div) // 10 # Update x by chopping off left and right digit. // x mod divider, then floor-divide by 10
            div /= 100 # Since x is updated, divider also needs to get updated // x got chopped off 2 digits, so must the divider
        
        return True