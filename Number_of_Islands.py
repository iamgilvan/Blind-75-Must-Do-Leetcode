import collections
import unittest
#TC O(n)
#TS O(n)
def number_of_islands(grid):
    if not grid:
        return 0

    islands = 0
    visited = set()
    rows, cols = len(grid), len(grid[0])

    def dfs(r, c):
        queue = collections.deque()
        visited.add((r, c))
        queue.append((r, c))

        while queue:
            directions = [[1,0], [-1, 0], [0, 1], [0, -1]]
            row, col = queue.popleft()
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if r in range(rows) and c in range(cols):
                    if grid[r][c] == '1' and (r, c) not in visited:
                        visited.add((r, c))
                        queue.append((r, c))

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == '1' and (row, col) not in visited:
                dfs(row, col)
                islands += 1

    return islands

class Test(unittest.TestCase):
    test_cases = [
        ([
            ["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]
        ], 1),
        ([
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
        ], 3),
    ]
    functions = [number_of_islands]
    def test_number_of_islands(self):
        for function in self.functions:
            for arr, expected in self.test_cases:
                result = function(arr)
                assert result == expected

if __name__ == '__main__':
    unittest.main()