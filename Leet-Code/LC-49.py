# Medium

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # mapping charCount to list of Anagrams // defaultdict(list) makes the values a list 
        
        for s in strs: # for every string in list strs
            count = [0] * 26 # a ... z // initialized to 26 0's
            
            for c in s: # for every character in that string
                count[ord(c) - ord("a")] += 1 # Increase value if character found // Ex) a is at index 0 b is at index 1
                
            res[tuple(count)].append(s) # Mapping the letter count to the string // Ex) aab => 2, 1, 0, 0 ... => "aab"
            # Strings with same letter count will be appended as a list
            
         
        return res.values() # Returning the values of hash map res