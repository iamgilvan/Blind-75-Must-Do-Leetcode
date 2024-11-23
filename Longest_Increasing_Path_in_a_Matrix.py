import collections
from typing import List
import unittest
# Given an m x n integers matrix, return the length of the longest increasing path in matrix.

# From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).
#TC O(m∗n∗4^m∗n)
#TS O(n*m)
def longest_increasing_path(grid):
    if not grid:
        return 0

    res = 0
    rows, cols = len(grid), len(grid[0])
    directions = [[1,0], [-1, 0], [0, 1], [0, -1]]
    def dfs(r, c, prevVal):
        if r not in range(rows) or not c in range(cols) or grid[r][c] <= prevVal:
            return 0
        path = 1
        for dr, dc in directions:
            row, col = r + dr, c + dc
            path = max(path,1 + dfs(row, col, grid[r][c]))
        return path
    for row in range(rows):
        for col in range(cols):
               res = max(res, dfs(row, col, float('-inf')))
    return res


#TC O(m∗n)
#TS O(n*m)
def longest_Increasing_Path(matrix: List[List[int]]) -> int:
    ROWS, COLS = len(matrix), len(matrix[0])
    dp = {}  # (r, c) -> LIP
    def dfs(r, c, prevVal):
        if (r < 0 or r == ROWS or c < 0 or 
            c == COLS or matrix[r][c] <= prevVal
        ):
            return 0
        if (r, c) in dp:
            return dp[(r, c)]
        res = 1
        res = max(res, 1 + dfs(r + 1, c, matrix[r][c]))
        res = max(res, 1 + dfs(r - 1, c, matrix[r][c]))
        res = max(res, 1 + dfs(r, c + 1, matrix[r][c]))
        res = max(res, 1 + dfs(r, c - 1, matrix[r][c]))
        dp[(r, c)] = res
        return res
    for r in range(ROWS):
        for c in range(COLS):
            dfs(r, c, -1)
    return max(dp.values())

class Test(unittest.TestCase):
    test_cases = [
        ([
            [9,9,4],
            [6,6,8],
            [2,1,1]
        ], 4),
        ([
            [3,4,5],
            [3,2,6],
            [2,2,1]
        ], 4),
    ]
    functions = [longest_increasing_path, longest_Increasing_Path]
    def test_longest_increasing_path(self):
        for function in self.functions:
            for arr, expected in self.test_cases:
                result = function(arr)
                assert result == expected

if __name__ == '__main__':
    unittest.main()