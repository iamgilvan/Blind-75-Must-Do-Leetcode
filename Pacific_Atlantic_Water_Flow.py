from collections import deque
import unittest

# There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

# The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

# The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

# Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

#TC O(N.M)
#TS O(N.M)
def pacific_atlantic(heights):
    ROWS, COLS = len(heights), len(heights[0])
    pac_seen, atl_seen = set(), set()
    pac_queue, atl_queue = deque(), deque()

    for col in range(COLS):
        pac_seen.add((0, col))
        pac_queue.append((0, col))

    for row in range(1, ROWS):
        pac_seen.add((row, 0))
        pac_queue.append((row, 0))

    for row in range(ROWS):
        atl_seen.add((row, COLS-1))
        atl_queue.append((row, COLS-1))

    for col in range(COLS-1):
        atl_seen.add((ROWS-1, col))
        atl_queue.append((ROWS-1, col))

    directions = [[1,0], [-1, 0], [0, 1], [0, -1]]
    def get_coords(q, seen):
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                row, col = r + dr, c + dc
                if row in range(ROWS) and col in range(COLS) and heights[row][col] >= heights[r][c] and (row, col) not in seen:
                    seen.add((row, col))
                    q.append((row, col))
        return seen
    p_coords = get_coords(pac_queue, pac_seen)
    q_coords = get_coords(atl_queue, atl_seen)

    return list(p_coords.intersection(q_coords))
#TC O(N.M)^2
#TS O(N.M)^2
def pacificAtlantic(heights):
    ROWS, COLS = len(heights), len(heights[0])
    pac, atl = set(), set()
    def dfs(r, c, visit, prevHeigth):

        if ((r, c) in visit or  #visited
        r < 0 or c < 0 or r == ROWS or c == COLS or # check out of index
        heights[r][c] < prevHeigth):
            return

        visit.add((r,c))
        dfs(r  + 1, c, visit, heights[r][c])
        dfs(r -  1, c, visit, heights[r][c])
        dfs(r, c + 1, visit, heights[r][c])
        dfs(r, c - 1, visit, heights[r][c])

    for c in range(COLS):
        dfs(0, c, pac, heights[0][c])
        dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

    for r in range(ROWS):
        dfs(r, 0, pac, heights[r][0])
        dfs(r, COLS - 1, atl, heights[r][c])

    return list(pac & atl)
    # return list(pac.intersection(atl))
    # res = []
    # for r in range(ROWS):
    #     for c in range(COLS):
    #         if (r, c) in atl and (r, c) in pac:
    #             res.append([r, c])
    # # return res

class Test(unittest.TestCase):
    test_cases = [
        ([
            [1,2,2,3,5],
            [3,2,3,4,4],
            [2,4,5,3,1],
            [6,7,1,4,5],
            [5,1,1,2,4]], [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]),
        ([[1]], [[0,0]]),
    ]
    functions = [pacific_atlantic]
    def test_pacificAtlantic(self):
        for function in self.functions:
            for heights, expected in self.test_cases:
                result = function(heights)
                assert result == expected

if __name__ == '__main__':
    unittest.main()