import unittest
import time
from copy import deepcopy


# O (NxN)
# O (1)
def rotate_matrix_algo(matrix):
    """rotates a matrix 90 degrees clockwise"""
    new_matrix = deepcopy(matrix)
    for i, row in enumerate(matrix):
        curr_row = 0
        for j, number in enumerate(row):
            curr_column = len(row) - i - 1
            new_matrix[curr_row][curr_column] = number
            curr_row += 1
    return new_matrix

# O (N^2)
# O (1)
def rotate_matrix_inplace(matrix):
    """Rotates a matrix 90 degrees clockwise in-place."""
    # Primeiro, faça a transposição da matriz (linhas se tornam colunas)
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Em seguida, inverta a ordem das colunas
    for i in range(len(matrix)):
        matrix[i].reverse()

    return matrix
# O (N^2)
# O (1)
def rotate_matrix_inplace_ii(matrix):
    """Rotates a matrix 90 degrees clockwise in-place."""
    # Primeiro, faça a transposição da matriz (linhas se tornam colunas)
    l, r = 0, len(matrix) - 1
    while l < r:
        for i in range (r - l):
            top, bottom = l, r
            matrix[top][l + i], matrix[bottom - i][l], matrix[bottom][r - i], matrix[top + i][r] = matrix[bottom - i][l], matrix[bottom][r - i], matrix[top + i][r], matrix[top][l + i]
        r -= 1
        l += 1
    return matrix
class Test(unittest.TestCase):
    test_cases = [
        (
            [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9],
            ],
            [
                [7, 4, 1],
                [8, 5, 2],
                [9, 6, 3],
            ]
        ),
        (
            [
                [1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 17, 18, 19, 20],
                [21, 22, 23, 24, 25],
            ],
            [
                [21, 16, 11, 6, 1],
                [22, 17, 12, 7, 2],
                [23, 18, 13, 8, 3],
                [24, 19, 14, 9, 4],
                [25, 20, 15, 10, 5],
            ],
        ),
    ]

    testable_functions = [
        rotate_matrix_algo,
        rotate_matrix_inplace,
        rotate_matrix_inplace_ii
    ]

    def test_rotate_matrix(self):
        for function in self.testable_functions:
            start = time.perf_counter()
            for matrix, expected in self.test_cases:
                actual = function(deepcopy(matrix))
                assert actual == expected, f"Failed {function.__name__} for: {[matrix]}"
            duration = time.perf_counter() - start
            print(f"{function.__name__} {duration * 1000:.1f}ms")

if __name__ == "__main__":
    unittest.main()