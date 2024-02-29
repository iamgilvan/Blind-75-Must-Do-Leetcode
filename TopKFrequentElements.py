import unittest

#TC O(nlogn)
def topKFrequentElements(nums, k):
    frequencies = {}
    for n in nums:
        if n in frequencies:
            frequencies[n] += 1
        else:
            frequencies[n] = 1
    s = sorted(frequencies, key=frequencies.get, reverse=True)
    res = s[:k]
    return res

class Test(unittest.TestCase):
    test_cases = [
        ([1,1,1,2,2,3], 2, [1, 2]),
        ([1], 1, [1]),
        ([4,1,-1,2,-1,2,3], 2, [-1, 2])
    ]
    functions = [topKFrequentElements]
    def test_topkfrequentElements(self):
        for function in self.functions:
            for nums, k, expected in self.test_cases:
                result = function(nums, k)
                assert result == expected

if __name__ == '__main__':
    unittest.main()