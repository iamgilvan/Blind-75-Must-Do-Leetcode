import unittest

# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

# Each number in candidates may only be used once in the combination.

# Note: The solution set must not contain duplicate combinations.

#TC O(n^2)
#TS O(1)
def combination_sum(arr, target):
    result = []
    arr.sort()
    def backtrack(cur, pos, target):
        if target == 0:
            result.append(cur.copy())
        if target < 0:
            return
        prev = -1
        for i in range(pos, len(arr)):
            if arr[i] == prev: continue
            cur.append(arr[i])
            backtrack(cur, i + 1, target - arr[i])
            cur.pop()
            prev = arr[i]
    backtrack([], 0, target)
    return result

def combination_sum_ii(candidates, target):
    res = []
    candidates.sort()
    def dfs(start, total, path):
        if total == 0:
            if path not in res:
                res.append(path.copy())
            return
        if total < 0:
            return
        for i in range(start, len(candidates)):
            path.append(candidates[i])
            dfs(i + 1, total - candidates[i], path)
            path.pop()
    dfs(0, target, [])
    return res

class Test(unittest.TestCase):
    test_cases = [
        ([10,1,2,7,6,1,5], 8, [[1,1,6],[1,2,5],[1,7],[2,6]]),
        ([2,5,2,1,2], 5, [[1,2,2],[5]]),
    ]
    functions = [combination_sum, combination_sum_ii]
    def test_combination_sum_II(self):
        for function in self.functions:
            for arr, target, expected in self.test_cases:
                result = function(arr, target)
                assert result == expected

if __name__ == '__main__':
    unittest.main()