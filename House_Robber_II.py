import unittest

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