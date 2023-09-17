import unittest

#time & space complexity O(NxM)
def spiral_matrix(matrix):

    if not matrix or len(matrix) == 0:
        return []
    rowBegin = 0
    rowEnd = len(matrix)
    columnBegin = 0
    columnEnd = len(matrix[0])
    result = []
    while rowBegin < rowEnd and columnBegin < columnEnd:
        # get every i in the top row
        for i in range(columnBegin, columnEnd):
            result.append(matrix[rowBegin][i])
        rowBegin += 1
        # get every i in the right col
        for i in range(rowBegin, rowEnd):
            result.append(matrix[i][columnEnd - 1])
        columnEnd -= 1

        if not (columnBegin < columnEnd and rowBegin < rowEnd):
            break
        # get every i in the bottom row
        for i in range(columnEnd - 1, columnBegin - 1, -1):
            result.append(matrix[rowEnd - 1][i])
        rowEnd -= 1

        # get every i in the left col
        for i in range(rowEnd - 1, rowBegin - 1, -1):
            result.append(matrix[i][columnBegin])
        columnBegin += 1

    return result

class Test(unittest.TestCase):
    test_cases = [
        ([ [1,2,3]
          ,[4,5,6]
          ,[7,8,9]
        ], [1,2,3,6,9,8,7,4,5]),
        ([ [1,2,3,4]
          ,[5,6,7,8]
          ,[9,10,11,12]
          ], [1,2,3,4,8,12,11,10,9,5,6,7]),
    ]
    functions = [spiral_matrix]
    def test_spiral_matrix(self):
        for function in self.functions:
            for arr, expected in self.test_cases:
                result = function(arr)
                assert result == expected

if __name__ == '__main__':
    unittest.main()