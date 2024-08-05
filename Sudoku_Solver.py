import collections
import unittest

# Write a program to solve a Sudoku puzzle by filling the empty cells.

# A sudoku solution must satisfy all of the following rules:

#     Each of the digits 1-9 must occur exactly once in each row.
#     Each of the digits 1-9 must occur exactly once in each column.
#     Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.

# The '.' character indicates empty cells.

# Example 1:

# Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
# Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
# Explanation: The input board is shown above and the only valid solution is shown below:
#TC O(9!^9) = O(1)
#SC O(1)
def sudoku_solver(arr):
    def is_valid(grid, r, c, k):
        not_in_row = str(k) not in grid[r]
        not_in_column = str(k) not in [grid[i][c] for i in range(9)]
        not_in_box = str(k) not in [grid[i][j] for i in range(r//3*3, r//3*3+3) for j in range (c//3*3, c//3*3+3)]
        return not_in_box and not_in_column and not_in_row
    def solve(grid, r=0, c=0 ):
        if r == 9:
            return True
        elif c == 9:
            return solve(grid, r + 1, 0)
        elif grid[r][c] != ".":
            return solve(grid, r, c + 1)
        else:
            for k in range(1, 10):
                if is_valid(grid, r, c, k):
                    grid[r][c] = str(k)
                    if solve(grid, r, c + 1):
                        return True
                    grid[r][c] = "."
        return False
    return solve(arr, 0, 0)

class Test(unittest.TestCase):
    test_cases = [
        ( [["5","3",".",".","7",".",".",".","."],
           ["6",".",".","1","9","5",".",".","."],
           [".","9","8",".",".",".",".","6","."],
           ["8",".",".",".","6",".",".",".","3"],
           ["4",".",".","8",".","3",".",".","1"],
           ["7",".",".",".","2",".",".",".","6"],
           [".","6",".",".",".",".","2","8","."],
           [".",".",".","4","1","9",".",".","5"],
           [".",".",".",".","8",".",".","7","9"]], 

         [["5","3","4","6","7","8","9","1","2"],
          ["6","7","2","1","9","5","3","4","8"],
          ["1","9","8","3","4","2","5","6","7"],
          ["8","5","9","7","6","1","4","2","3"],
          ["4","2","6","8","5","3","7","9","1"],
          ["7","1","3","9","2","4","8","5","6"],
          ["9","6","1","5","3","7","2","8","4"],
          ["2","8","7","4","1","9","6","3","5"],
          ["3","4","5","2","8","6","1","7","9"]]),
    ]
    functions = [sudoku_solver]
    def test_sudoku_solver(self):
        for function in self.functions:
            for arr, expected in self.test_cases:
                result = function(arr)
                assert arr == expected

if __name__ == '__main__':
    unittest.main()