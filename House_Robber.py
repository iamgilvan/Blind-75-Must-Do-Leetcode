import unittest

# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
#TC O(n)
#TS O(1)
def house_robber(arr):
    rob1, rob2 = 0,0
    for i in arr:
        temp = max(i + rob1, rob2)
        rob1 = rob2
        rob2 = temp

    return rob2

class Test(unittest.TestCase):
    test_cases = [
        ([1,2,3,1], 4),
        ([2,7,9,3,1], 12),
    ]
    functions = [house_robber]
    def test_house_robber(self):
        for function in self.functions:
            for arr, expected in self.test_cases:
                result = function(arr)
                assert result == expected

if __name__ == '__main__':
    unittest.main()