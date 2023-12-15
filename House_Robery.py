import unittest

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