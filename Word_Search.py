
import unittest
# time complexity :  O(m * n * 4^L)
def word_search(arr, word):
    rows, cols = len(arr), len(arr[0])
    visited = set()

    def dfs(row, col, i):
        if i == len(word):
            return True;
        # check out of bound
        if row < 0 or col < 0 or row >= rows or col >= cols:
            return False;

        # check if visited or is not the word
        if word[i] != arr[row][col] or (row, col) in visited:
            return False;
        visited.add((row, col))

        result = (dfs(row + 1, col, i + 1) or
                dfs(row - 1, col, i + 1) or
                dfs(row, col + 1, i + 1) or
                dfs(row, col - 1, i + 1))

        visited.remove((row, col))
        return result

    for i in range(rows):
        for j in range(cols):
            if dfs(i, j, 0): return True
    return False

class Test(unittest.TestCase):
    test_cases = [
        ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],  "ABCCED", True),
        ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],  "SEE", True),
        ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],  "ABCB", False),
    ]
    functions = [word_search]
    def test_climbing_stairs(self):
        for function in self.functions:
            for arr, word, expected in self.test_cases:
                result = function(arr, word)
                assert result == expected

if __name__ == '__main__':
    unittest.main()