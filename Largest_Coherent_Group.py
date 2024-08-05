import collections
import unittest

# In a two-dimensional array, containing 0s and 1s, find the largest coherent group of 1s 
# (two 1s are coherent if they are placed next to each other in a direction N, E, S, or W).
#TC O(m×n)
def largest_coherent_group(matrix):
    if not matrix or not matrix[0]:
        return 0
    rows, cols = len(matrix), len(matrix[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    largest_group_size = 0
    # Possible movements (N, E, S, W)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    def dfs(matrix, visited, x, y):
        stack = [(x, y)]
        visited[x][y] = True
        size = 0
        while stack:
            cx, cy = stack.pop()
            size += 1
            # Explore all four directions
            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < len(matrix) and 0 <= ny < len(matrix[0]) and not visited[nx][ny] and matrix[nx][ny] == 1:
                    visited[nx][ny] = True
                    stack.append((nx, ny))
        return size

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1 and not visited[i][j]:
                # Start a DFS to find the size of this connected component
                group_size = dfs(matrix, visited, i, j)
                largest_group_size = max(largest_group_size, group_size)

    return largest_group_size

class Test(unittest.TestCase):
    test_cases = [
        (
            [
                [1, 1, 0, 0],
                [0, 1, 1, 0],
                [0, 0, 1, 0],
                [1, 0, 0, 0]
            ]
         , 5),
    ]
    functions = [largest_coherent_group]
    def test_largest_coherent_group(self):
        for function in self.functions:
            for arr, expected in self.test_cases:
                result = function(arr)
                assert result == expected

if __name__ == '__main__':
    unittest.main()