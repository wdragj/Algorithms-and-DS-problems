# Easy

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower() # change string to lower case only
        listS = []
        
        for letters in s:
            if letters.isalnum(): # if letter is alphanumeric
                listS.append(letters) # append to list
        
        left, right = 0, len(listS)-1 # first and last index is defined as left and right
        
        while left < right:
            if listS[left] != listS[right]:
                return False
            elif listS[left] == listS[right]:
                left += 1
                right -= 1
            else:
                return False
        return True