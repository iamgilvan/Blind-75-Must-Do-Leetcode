import unittest
# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

#TC O(n)
#TS O(1)
def house_robber(arr):
    def helper(arr):
        h1, h2 = 0,0
        for i in arr:
            temp = max(i + h1, h2)
            h1 = h2
            h2 = temp
        return h2

    return max(arr[0], helper(arr[1:]), helper(arr[:-1]))

class Test(unittest.TestCase):
    test_cases = [
        ([2,3,2], 3),
        ([1,2,3,1], 4),
        ([1,2,3], 3)
    ]
    functions = [house_robber]
    def test_house_robber(self):
        for function in self.functions:
            for arr, expected in self.test_cases:
                result = function(arr)
                assert result == expected

if __name__ == '__main__':
    unittest.main()