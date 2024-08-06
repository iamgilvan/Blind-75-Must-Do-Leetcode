from collections import deque
import unittest

#TC: (n.m)
#TS : O(n)
def wall_and_gates(grid):
    ROWS, COLS = len(grid), len(grid[0])
    visit = set()
    q = deque()
    def addCell(r, c):
        if (
            min(r, c) < 0
            or r == ROWS
            or c == COLS
            or (r, c) in visit
            or grid[r][c] == -1
        ):
            return
        visit.add((r, c))
        q.append([r, c])
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 0:
                q.append([r, c])
                visit.add((r, c))
    dist = 0
    while q:
        for i in range(len(q)):
            r, c = q.popleft()
            grid[r][c] = dist
            addCell(r + 1, c)
            addCell(r - 1, c)
            addCell(r, c + 1)
            addCell(r, c - 1)
        dist += 1

class Test(unittest.TestCase):
    test_cases = [
        ([
        [2147483647,-1,0,2147483647],
        [2147483647,2147483647,2147483647,-1],
        [2147483647,-1,2147483647,-1],
        [0,-1,2147483647,2147483647]
        ], [
            [3,-1,0,1],
            [2,2,1,-1],
            [1,-1,2,-1],
            [0,-1,3,4]
            ]),
        ([
        [0,-1],
        [2147483647,2147483647]
        ], [
            [0,-1],
            [1,2]
            ])
    ]
    functions = [wall_and_gates]
    def test_wall_and_gates(self):
        for function in self.functions:
            for arr, expected in self.test_cases:
                function(arr)
                assert arr == expected

if __name__ == '__main__':
    unittest.main()