# Medium

# Solution 1
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # O(m log n)
        for arr in matrix:
            l, r = 0, len(arr) - 1
            
            while l <= r:
                mid = (l+r) // 2
                if arr[mid] == target:
                    return True
                
                if arr[mid] > target:
                    r = mid - 1
                else: # arr[mid] < target
                    l = mid + 1
        
        return False

# Solution 2
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # O(log m + log n)
        
        ROW, COL = len(matrix), len(matrix[0])
        
        top, bot = 0, ROW - 1
        
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break
        
        if not (top <= bot):
            return False
        
        l, r = 0, COL - 1
        
        while l <= r:
            mid = (l + r) // 2

            if matrix[row][mid] > target:
                r = mid - 1
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                return True