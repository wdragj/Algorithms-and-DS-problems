# There are three types of edits that can be performed on strings
# 1. Insert a character
# 2. Remove a character
# 3. Replace a character
# Given two strings, write a function to check if they are one edit (or zero edits) away

def one_away(original, edited):
  # Base case
  if abs(len(original) - len(edited)) > 1: return False

  # Insert a character // Different length
  # Remove a character // Different length
  # Replace a character // Same length
  p1, p2 = 0, 0
  madeEdit = False
  while p1 < len(original) and p2 < len(edited):
    if original[p1] == edited[p2]:
      p1 += 1
      p2 += 1
    elif not madeEdit: # Characters are different and there hasn't been a change
      madeEdit = True
      if len(original) == len(edited): # If same length // Assume there is a replace
        p1 += 1
        p2 += 1
      elif len(original) > len(edited): # Original is longer // Assume there is an insert in original || deletion in edited
        p1 += 1
      elif len(original) < len(edited): # Edited is longer // Assume there is an insert in edited || deletion in original
        p2 += 1
    else:
      return False # Entering this condition means there has been more than one edit
  
  return True # If reached, means one or no change at all

print(one_away("pale", "ple"))
print(one_away("pales", "pale"))
print(one_away("pale", "bale"))
print(one_away("pale", "bake"))