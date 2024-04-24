import collections
import unittest
import math

#TC O(9^2) == O(81) == O(1)
#SC O(1)
def valid_sudoku(arr):
    cols = collections.defaultdict(set)
    rows = collections.defaultdict(set)
    squares = collections.defaultdict(set) # key = (r/3, c/3)

    for r in range(9):
        for c in range(9):
            if arr[r][c] == ".": continue

            if (arr[r][c] in rows[r] or
                arr[r][c] in cols[c] or
                arr[r][c] in squares[(r//3, c//3)]):
                return False
            cols[c].add(arr[r][c])
            rows[r].add(arr[r][c])
            squares[(r//3, c//3)].add(arr[r][c])
    return True

class Test(unittest.TestCase):
    test_cases = [
        ([["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]], True),

        ([["8","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]], False),
    ]
    functions = [valid_sudoku]
    def test_valid_sudoku(self):
        for function in self.functions:
            for arr, expected in self.test_cases:
                result = function(arr)
                assert result == expected

if __name__ == '__main__':
    unittest.main()