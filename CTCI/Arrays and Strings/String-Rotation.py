# Assume you have a method isSubstring which checks if one word is a substring of another
# Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring
# Ex) waterbottle is a rotation of erbottlewat

def isSubstring(s1, s3):
  if s1 in s3:
    return True
  else:
    return False

def isRotation(s1, s2):
  return isSubstring(s1, s2 + s2)

s1 = "waterbottle"
s2 = "erbottlewat"

print(isRotation(s1, s2))
print(isRotation("CodingInterview", "erviewCodingInt"))
print(isRotation("Test", "est"))