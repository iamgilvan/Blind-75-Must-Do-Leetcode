import collections
import unittest

class ListNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
class Tree:
    def __init__(self):
        self.root = ListNode()

    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = ListNode()
            current = current.children[char]
        current.is_end_of_word = True

    def search(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_end_of_word

    def startWith(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return True

def word_search_ii(grid, words):
    words_found = []
    visited = set()
    rows, cols = len(grid), len(grid[0])

    tree = Tree()
    for word in words:
        tree.insert(word)

    word = ''
    def dfs(r, c, word):
        visited.add((r, c))
        queue = collections.deque()
        queue.append((r, c))

        while queue:
            directions = [[1,0], [-1, 0], [0, 1], [0, -1]]
            row, col = queue.popleft()
            for dr, dc in directions:
                r, c  = row + dr, col + dc
                # check if is out of range
                if r in range(rows) and c in range(cols):
                    temp = word + grid[r][c]
                    if tree.startWith(temp) and (r, c) not in visited:
                        word += grid[r][c]
                        visited.add((r, c))
                        queue.append((r, c))
                        if tree.search(word) and word not in words_found:
                            words_found.append(word)
                            word = word[:-1]
                            visited.remove((r, c))
        return word

    for row in range(rows):
        for col in range(cols):
            if tree.startWith(grid[row][col]):
                word += grid[row][col]
                w = dfs(row, col, word)
                if tree.search(w) and w not in words_found:
                    words_found.append(w)
                word = ''
        visited.clear()

    return words_found


def find_words(grid, words):
    words_found = set()
    visited = set()
    rows, cols = len(grid), len(grid[0])

    tree = Tree()
    for word in words:
        tree.insert(word)

    def dfs(r, c, node, word):
        if not (0 <= r < rows and 0 <= c < cols) or (r, c) in visited or grid[r][c] not in node.children:
            return

        visited.add((r, c))
        node = node.children[grid[r][c]]
        word += grid[r][c]
        if node.is_end_of_word and word not in words_found:
            words_found.add(word)

        dfs(r + 1, c, node, word)
        dfs(r - 1, c, node, word)
        dfs(r , c + 1, node, word)
        dfs(r , c - 1, node, word)

        visited.remove((r, c))

    for row in range(rows):
        for col in range(cols):
            dfs(row, col, tree.root, '')

    return list(words_found)

class Test(unittest.TestCase):
    test_cases = [
        (
            [
            ["o","a","a","n"],
            ["e","t","a","e"],
            ["i","h","k","r"],
            ["i","f","l","v"]
          ]
         , ["oath","pea","eat","rain"], ["oath", "eat"]),
        (
            [
                ["a","b"],["c","d"]
            ], ["abcb"], []
        ),
        (
            [
                ["o","a","a","n"],
                ["e","t","a","e"],
                ["i","h","k","r"],
                ["i","f","l","v"],
            ], ["oath","pea","eat","rain","hklf", "hf"], ["oath","eat","hf", "hklf"]
        ), 
    ]
    functions = [find_words]
    def test_number_of_islands(self):
        for function in self.functions:
            for arr, words, expected in self.test_cases:
                result = function(arr, words)
                assert result == expected

if __name__ == '__main__':
    unittest.main()