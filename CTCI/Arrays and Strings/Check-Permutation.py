# Given two strings, write a method to decide if one is a permutation of the other.
# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
# In other words, return true if one of s1's permutations is the substring of s2.

def isPermuation(s1, s2):
  if len(s1) > len(s2): return False

  s1count, s2count = [0] * 26, [0] * 26

  for i in range(len(s1)):
    s1count[ord(s1[i]) - ord("a")] += 1
    s2count[ord(s2[i]) - ord("a")] += 1
  
  matches = 0
  for i in range(26):
    matches += (1 if s1count[i] == s2count[i] else 0)
  
  l = 0
  for r in range(len(s1), len(s2)):
    if matches == 26: return True

    index = ord(s2[r]) - ord("a")
    s2count[index] += 1
    if s1count[index] == s2count[index]:
      matches += 1
    elif s1count[index] + 1 == s2count[index]:
      matches -= 1
    
    index = ord(s2[l]) - ord("a")
    s2count[index] -= 1
    if s1count[index] == s2count[index]:
      matches += 1
    elif s1count[index] - 1 == s2count[index]:
      matches -= 1
    
    l += 1
  
  return matches == 26

s1 = "ab"
s2 = "eidbaooo"
print(isPermuation(s1, s2))