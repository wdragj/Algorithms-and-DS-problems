# Easy

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "": # If needle is empty, return 0
            return 0
        
        for i in range(len(haystack) - len(needle) + 1): # For loop from 0 to the needed index to check length of needle
            if haystack[i: i + len(needle)] == needle: # If the sliced string at i is equal to needle
                return i # return the index of i
        
        return -1 # If return not reached in for loop, haystack doesn't contain needle