# Given an image represented by an NxN matrix
# Where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees
# Can you do this in place?

def rotateImg(matrix):
  for i in range(len(matrix)):
    for j in range(i + 1, len(matrix)):
      # Switch the row and column indices
      matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
  
  # Reverse every row
  for r in range(len(matrix)):
    for i in range(len(matrix[r]) // 2):
      # oppI is the opposing index to i
      oppI = len(matrix[r]) - 1 - i
      matrix[r][i], matrix[r][oppI] = matrix[r][oppI], matrix[r][i]
  
  for arr in matrix:
    print(arr)

rotateImg([[ 5, 1, 9,11], [ 2, 4, 8,10], [13, 3, 6, 7], [15,14,12,16]])