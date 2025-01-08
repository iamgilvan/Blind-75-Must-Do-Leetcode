from copy import deepcopy
import unittest

# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

# You must do it in place.
# Example 1:

# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]

# Example 2:

# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

# Time complexity O(n * m) : Space Complexity O(n * m)
def set_zeros(matrix):
    rows_to_set = set()
    columns_to_set = set()
    for row in range(len(matrix)):
        if 0 in matrix[row]:
            rows_to_set.add(row)
        for column in range(len(matrix[row])):
            if 0 == matrix[row][column]:
                columns_to_set.add(column)

    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if row in rows_to_set or column in columns_to_set:
                matrix[row][column] = 0
    return matrix


def set_zero_ii(matrix):

    cordinates_to_set = set()
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if 0 == matrix[row][column]:
                cordinates_to_set.add((row, column))

    for row, column in cordinates_to_set:
        for i in range(len(matrix[0])):
            matrix[row][i] = 0
        for j in range(len(matrix)):
            matrix[j][column] = 0
    return matrix

class Test(unittest.TestCase):
    test_cases = [
        ([[0,1,2,0],
          [3,4,5,2],
          [1,3,1,5]],

         [[0,0,0,0],
          [0,4,5,0],
          [0,3,1,0]]),
        ([[1,1,1],[1,0,1],[1,1,1]], [[1,0,1],[0,0,0],[1,0,1]])
    ]
    functions = [set_zeros, set_zero_ii]
    def test_climbing_stairs(self):
        for function in self.functions:
            for matrix, expected in self.test_cases:
                result = function(deepcopy(matrix))
                assert result == expected

if __name__ == '__main__':
    unittest.main()