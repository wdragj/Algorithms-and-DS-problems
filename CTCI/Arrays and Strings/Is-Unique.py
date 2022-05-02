# Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?

# Store the letters in the string into a hash table

def uniqueChar(string):
  hashChar = {}

  for l in string:
    hashChar[l] = hashChar.get(l, 0) + 1
  
  for value in hashChar.values():
    if value != 1:
      return False
  
  return True

print(uniqueChar("Hello"))
print(uniqueChar("Hi"))
print(uniqueChar("watermelon"))
print(uniqueChar("blue"))