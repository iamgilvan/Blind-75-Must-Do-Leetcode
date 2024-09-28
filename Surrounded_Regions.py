from collections import deque
import unittest

# You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

#     Connect: A cell is connected to adjacent cells horizontally or vertically.
#     Region: To form a region connect every 'O' cell.
#     Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.

# A surrounded region is captured by replacing all 'O's with 'X's in the input matrix board.
#TC O(N.M)
#TS O(N.M)

def surrounded_regions(board):
    ROWS, COLS = len(board), len(board[0])
    directions = [[1,0], [-1, 0], [0, 1], [0, -1]]
    def capture_board(r, c):
        if r in range(ROWS) and c in range(COLS) and board[r][c] == "O":
            board[r][c] = "B"
            for dr, dc in directions:
                capture_board(r + dr, c + dc)

    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == "O" and (row in [0, ROWS -1] or col in [0, COLS -1]):
                capture_board(row, col)

    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == "O":
                board[row][col] = "X"
            elif board[row][col] == "B":
                board[row][col] = "O"
    return board

class Test(unittest.TestCase):
    test_cases = [
        ([
            ["X","X","X","X"],
            ["X","O","O","X"],
            ["X","X","O","X"],
            ["X","O","X","X"]
        ],
         [
            ["X","X","X","X"],
            ["X","X","X","X"],
            ["X","X","X","X"],
            ["X","O","X","X"]
         ]
         ),
        ([["X","X","X"],["X","O","X"],["X","X","X"]], [["X","X","X"],["X","X","X"],["X","X","X"]]),
        ([["X"]], [["X"]]),
    ]
    functions = [surrounded_regions]
    def test_surrounded_regions(self):
        for function in self.functions:
            for board, expected in self.test_cases:
                result = function(board)
                assert result == expected

if __name__ == '__main__':
    unittest.main()