import unittest

# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

# There is only one repeated number in nums, return this repeated number.

# You must solve the problem without modifying the array nums and uses only constant extra space.
#TC O(n)
#TS O(n)
def findDuplicate(nums):
    visited = []
    left, right = 0, len(nums) -1
    while left <= right:
        if nums[left] == nums[right]:
            return nums[left]
        if nums[left] in visited:
            return nums[left]
        if nums[right] in visited:
            return nums[right]
        visited += [nums[left], nums[right]]
        left += 1
        right -= 1
    return -1
#TC O(n)
#TS O(1)
def find_duplicate(nums):
    for i in range(len(nums)):
        if nums.index(nums[i]) < i:
            return nums[i]
    return -1
#TC O(n)
#TS O(1)
def find_duplicate_ll(nums):
    fast, slow = 0, 0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    slow2 = 0
    while True:
        slow = nums[slow]
        slow2 = nums[slow2]
        if slow == slow2:
            return slow

class Test(unittest.TestCase):
    test_cases = [
        ([1,2,3,1], 1),
        ([1,3,4,2,2], 2),
        ([3,1,3,4,2], 3),
        ([3,3,3,3,3], 3)
    ]
    functions = [findDuplicate, find_duplicate, find_duplicate_ll]
    def test_find_duplicates_number(self):
        for function in self.functions:
            for arr, expected in self.test_cases:
                result = function(arr)
                assert result == expected

if __name__ == '__main__':
    unittest.main()