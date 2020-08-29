
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]

def searchMatrix(matrix, target):
    m = len(matrix) # number of rows
    n = len(matrix[0]) # number of columns
    
    if target > matrix[m-1][n-1] or target < matrix[0][0]:
        return False
    
    col = n - 1
    row = 0

    while col >= 0 and row <= m - 1:
        if matrix[row][col] < target:
            row += 1
        elif matrix[row][col] > target:
            col -= 1
        else:
            return True
    return False

searchMatrix(matrix,1)