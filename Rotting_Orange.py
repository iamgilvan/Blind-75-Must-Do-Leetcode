from collections import deque
import unittest

# You are given an m x n grid where each cell can have one of three values:

#     0 representing an empty cell,
#     1 representing a fresh orange, or
#     2 representing a rotten orange.

# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

#TC O(n^2)
#TS O(1)
def rotting_oranges(grid):
    time, fresh = 0, 0
    ROWS, COLS = len(grid), len(grid[0])
    q = deque()

    directions = [[1,0], [-1, 0], [0, 1], [0, -1]]
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 1:
                fresh += 1
                continue
            if grid[r][c] == 2:
                q.append((r, c))
    while q and fresh > 0:
        for _ in range(len(q)):
            r, c = q.popleft()
            for dr, dc in directions:
                row, col = dr + r, dc + c
                # if in bounds and frash, make rotten
                if row not in range(ROWS) or col not in range(COLS) or grid[row][col] != 1:
                    continue
                grid[row][col] = 2
                q.append((row, col))
                fresh -= 1
        time += 1
    return time if fresh == 0 else -1

class Test(unittest.TestCase):
    test_cases = [
        ([[2,1,1],[1,1,0],[0,1,1]], 4),
        ([[2,1,1],[0,1,1],[1,0,1]], -1),
        ([[0,2]],0),
        ([[2],[1]], 1)
    ]
    functions = [rotting_oranges]
    def test_rotting_oranges(self):
        for function in self.functions:
            for arr, expected in self.test_cases:
                result = function(arr)
                assert result == expected

if __name__ == '__main__':
    unittest.main()