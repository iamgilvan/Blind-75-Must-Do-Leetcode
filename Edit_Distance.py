import unittest

# Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

# You have the following three operations permitted on a word:

#     Insert a character
#     Delete a character
#     Replace a character

#TC O(m * n)
#TS O(m * n)
def edit_distance(s: str, t: str) -> int:
    cache = {}
    def dfs(i, j):
        if i == len(s): return len(t) - j
        if j == len(t): return len(s) - i

        if (i, j) in cache:
            return cache[(i,j)]
        if s[i] == t[j]:
            cache[(i,j)] = dfs(i + 1, j + 1)
        else:
            #insert and #delete
            cache[(i,j)] = min(dfs(i, j + 1), dfs(i + 1, j))
            # replace
            cache[(i,j)] = min(cache[(i,j)], dfs(i + 1, j + 1))
            cache[(i,j)] = cache[(i,j)] + 1
        return cache[(i,j)]
    return dfs(0,0)

#TC O(m * n)
#TS O(min(m, n))
def min_distance_optiomal(word1: str, word2: str) -> int:
    m, n = len(word1), len(word2)
    if m < n:
        m, n = n, m
        word1, word2 = word2, word1
    cache = [n - i for i in range(n + 1)]
    for i in range(m - 1, -1, -1):
        nextVal = cache[n]
        cache[n] = m - i
        for j in range(n - 1, -1, -1):
            temp = cache[j]
            if word1[i] == word2[j]:
                cache[j] = nextVal
            else:
                cache[j] = 1 + min(cache[j], cache[j + 1], nextVal)
            nextVal = temp
    return cache[0]

class Test(unittest.TestCase):
    test_cases = [
        ("horse", "ros",  3),
        ("intention", "execution", 5),
    ]
    functions = [edit_distance, min_distance_optiomal]
    def test_edit_distance(self):
        for function in self.functions:
            for s1, s2, expected in self.test_cases:
                result = function(s1, s2)
                assert result == expected

if __name__ == '__main__':
    unittest.main()