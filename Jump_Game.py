import unittest

# You are given an array of integers nums, where nums[i] represents the maximum length of a jump towards the right from index i. For example, if you are at nums[i], you can jump to any index i + j where:

#     j <= nums[i]
#     i + j < nums.length

# You are initially positioned at nums[0].

# Return the minimum number of jumps to reach the last position in the array (index nums.length - 1). You may assume there is always a valid answer

#time complexity O(N) : space complexity O(1)
def jump_game(nums):
    res = 0
    l = r = 0
    while r < len(nums) - 1:
        farthest = 0
        for i in range(l, r + 1):
            farthest = max(farthest, i + nums[i])
        l = r + 1
        r = farthest
        res += 1
    return res

#time complexity O(N!) : space complexity O(N)
def jump_game_ii(nums):
    def dfs(i):
        if i == len(nums) - 1:
            return 0
        if nums[i] == 0:
            return float('inf')
        end = min(len(nums) - 1, i + nums[i])
        res = float('inf')
        for j in range(i + 1, end + 1):
            res = min(res, 1 + dfs(j))
        return res
    return dfs(0)

class Test(unittest.TestCase):
    test_cases = [
        ([2,3,1,1,4], 2),
        ([2,3,0,1,4], 2),
        ([2,4,1,1,1,1], 2),
        ([2,1,2,1,0], 2)
    ]
    functions = [jump_game, jump_game_ii]
    def test_can_jump(self):
        for function in self.functions:
            for arr, expected in self.test_cases:
                result = function(arr)
                assert result == expected

if __name__ == '__main__':
    unittest.main()