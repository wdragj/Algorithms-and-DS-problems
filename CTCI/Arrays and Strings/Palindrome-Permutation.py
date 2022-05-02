# Given a string, write a function to check if it is a permutation of a palindrome.
# A palindrome is a word or phrase that is the same forwards and backwards.
# A permutation is a rearrangement of letters.
# The palindrome does not need to be limited to just dictionary words.

def pal_permutation(string):
  hashCount = {}

  string = string.replace(" ", "").lower()

  for l in string:
    hashCount[l] = hashCount.get(l, 0) + 1
  
  hasOdd = False
  for c in hashCount.values():
    if c % 2 == 1:
      if hasOdd:
        return False
      hasOdd = True
  
  return True

print(pal_permutation("Tact Coa"))
print(pal_permutation("Hello"))
print(pal_permutation("elle"))

