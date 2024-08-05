# Given an integer array nums and an integer k, return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Can you solve it without sorting?

# Example 1:

# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5

# Example 2:

# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4

import heapq
import unittest

# TC: O(N∗Log(K))

def find_kth_largest(nums, k):
    return heapq.nlargest(k, nums)[-1]

def find_kth_largest_ii(nums, k):
    heap = []
    for num in nums:
        heapq.heappush(heap,-num)
    while k > 0:
        res = heapq.heappop(heap)
        k -=1
    return -res

# TC: O(N^2)
def find_kth_largest_iiI(nums, k):
    k = len(nums) - k

    def quick_select(l, r):
        pivot, p = nums[r], l
        for i in range(l,r):
            if nums[i] <= pivot:
                nums[p], nums[i] = nums[i], nums[p]
                p +=1
        nums[p], nums[r] = nums[r], nums[p]
        if p > k : return quick_select(l, p - 1)
        elif p < k: return quick_select(p + 1, r)
        else: return nums[p]
    return quick_select(0, len(nums) - 1)

class Test(unittest.TestCase):
    test_cases = [
        ([3,2,1,5,6,4], 2, 5),
        ([3,2,3,1,2,4,5,5,6], 4, 4),
    ]
    functions = [find_kth_largest, find_kth_largest_ii, find_kth_largest_iiI]
    def test_find_kth_largest(self):
        for function in self.functions:
            for arr,k, expected in self.test_cases:
                result = function(arr, k)
                assert result == expected

if __name__ == '__main__':
    unittest.main()