# Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0

def zeroMatrix(matrix):
  for r in range(len(matrix)):
    for c in range(len(matrix[r])):
      if matrix[r][c] == 0:
        setNone(matrix, r, c)
  
  for r in range(len(matrix)):
    for c in range(len(matrix[r])):
      if matrix[r][c] == None:
        matrix[r][c] = 0

  for arr in matrix:
    print(arr)

def setNone(matrix, r, c):
  for i in range(len(matrix[r])):
    if matrix[r][i] != 0:
      matrix[r][i] = None
  
  for i in range(len(matrix)):
    if matrix[i][c] != 0:
      matrix[i][c] = None
  
  matrix[r][c] = None

zeroMatrix([
  [1,2,3,4],
  [5,0,7,8],
  [6,1,1,2],
  [2,3,4,1]
  ])