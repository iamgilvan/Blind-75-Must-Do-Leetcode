import unittest

# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

#TC O(nlogn)
#TS O(1)
def contains_duplicates(arr):
    arr.sort()
    for i in range(0, len(arr) - 1):
        if arr[i] == arr[i + 1]:
            return True
    return False

#TC O(n)
#TS O(n)
def contains_duplicates_hashset(arr):
    hashset = set()
    for i in arr:
        if i in hashset:
            return True
        hashset.add(i)
    return False

class Test(unittest.TestCase):
    test_cases = [
        ([1,2,3,1], True),
        ([1,2,3,4], False),
        ([1,1,1,3,3,4,3,2,4,2], True)
    ]
    functions = [contains_duplicates, contains_duplicates_hashset]
    def test_contains_duplicates(self):
        for function in self.functions:
            for arr, expected in self.test_cases:
                result = function(arr)
                assert result == expected

if __name__ == '__main__':
    unittest.main()