import unittest
# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

# The test cases are generated so that the answer will be less than or equal to 2 * 109.

# Example 1:

# Input: m = 3, n = 7
# Output: 28

# Example 2:

# Input: m = 3, n = 2
# Output: 3
# Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down

#O(m * n) : O(m * n)
def unique_path(rows, columns):
    if columns == rows == 1:
        return 1
    matrix = [[1 for _ in range(columns)] for _ in range(rows)]
    for row in range(1, len(matrix)):
        for col in range(1, len(matrix[row])):
            matrix[row][col] = matrix[row][col - 1] + matrix[row - 1][col]
    return matrix[rows - 1][columns - 1]


# Time complexity: O(2m+n)O(2m+n)
# Space complexity: O(m+n)O(m+n)
def uniquePaths(rows, columns):
    def dfs(i, j):
        if i == (rows - 1) and j == (columns - 1):
            return 1
        if i >= rows or j >= columns:
            return 0
        return dfs(i, j + 1) + dfs(i + 1, j)
    return dfs(0, 0)

class Test(unittest.TestCase):
    test_cases = [
        (3, 7, 28),
        (3, 2, 3)
    ]
    functions = [unique_path, uniquePaths]
    def test_unique_path(self):
        for function in self.functions:
            for m, n, expected in self.test_cases:
                result = function(m, n)
                assert result == expected

if __name__ == '__main__':
    unittest.main()