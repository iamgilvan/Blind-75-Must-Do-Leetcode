import unittest
# Given an integer array nums that may contain duplicates, return all possible
# subsets
# (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.
#TC  O(n)
#SC O(1)
def permutations(nums):
    m_res = []
    def dfs(n):
        if len(n) == 0:
            return [[]]
        perms = dfs(n[1:])
        res = []
        for p in perms:
            for i in range(len(p) + 1):
                p_copy = p.copy()
                p_copy.insert(i, n[0])
                res.append(p_copy)
        return res
    m_res = dfs(nums)
    return m_res

class Test(unittest.TestCase):
    test_cases = [
        ([1,2,3],[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]),
        ([0,1], [[0,1],[1,0]]),
        ([1], [[1]]),
    ]
    functions = [permutations]
    def test_permutation(self):
        for function in self.functions:
            for s, expected in self.test_cases:
                result = function(s)
                assert result == expected

if __name__ == '__main__':
    unittest.main()