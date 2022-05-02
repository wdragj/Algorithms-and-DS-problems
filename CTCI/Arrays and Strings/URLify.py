# Write a method to replace all spaces in a string with "%20" 
# You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given the "true" length of the string.

def URLify(string, length):
  string = string[:length]
  string = string.replace(" ", "%20")

  return string

print(URLify("Mr John Smith      ", 13))