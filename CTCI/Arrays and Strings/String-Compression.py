# Implement a method to perform basic string compression using the counts of repeated characters
# Ex) the string aabcccccaaa would become a2b1c5a3
# If the compressed string would not become smaller than the original string, your method should return the original string
# You can assume the string has only uppercase and lowercase letters (a-z)

def strComp(string):
  compressSTR = []
  curr = string[0]
  cnt = 1
  for l in string[1:]:
    if curr == l:
      cnt += 1
    else:
      compressSTR.append(curr)
      compressSTR.append(str(cnt))
      curr = l
      cnt = 1
  compressSTR.append(curr)
  compressSTR.append(str(cnt))
  
  compressSTR = "".join(compressSTR)

  if len(compressSTR) > len(string):
    return string
  else:
    return compressSTR

print(strComp("aabcccccaaa"))