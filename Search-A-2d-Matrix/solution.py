class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROW, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROW - 1
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            
            elif target < matrix[row][0]:
                bot = row - 1
            
            else:
                break
        
        if not(top <= bot):
            return False
        
        row = (top + bot) // 2
        left, right = 0, COLS - 1
        while left <= right:
            middle = (left + right) // 2
            if matrix[row][middle] > target:
                right = middle - 1            
            elif matrix[row][middle] < target:
                left = middle + 1
            
            else:
                return True
        
        return False