import collections
import unittest
# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

# The area of an island is the number of cells with a value 1 in the island.

# Return the maximum area of an island in grid. If there is no island, return 0.
#TC O(n)
#TS O(n)
def max_area_of_island(grid):
    if not grid: return 

    rows, cols = len(grid), len(grid[0])
    max_res = 0
    visited = set()
    def dfs(r, c):
        if r not in range(rows) or c not in range(cols) or grid[r][c] == 0 or (r,c) in visited:
            return 0
        visited.add((r,c))
        return (1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r , c + 1) + dfs(r , c - 1))
    for row in range(rows):
        for col in range(cols):
            max_res = max(max_res, dfs(row, col))
    return max_res

class Test(unittest.TestCase):
    test_cases = [
        ([
            [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
        ], 9),
        ([
            [[0,0,0,0,0,0,0,0]]
        ],0),
    ]
    functions = [max_area_of_island]
    def test_max_area_of_island(self):
        for function in self.functions:
            for arr, expected in self.test_cases:
                result = function(arr)
                assert result == expected

if __name__ == '__main__':
    unittest.main()