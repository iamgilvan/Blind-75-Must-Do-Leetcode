# Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Implement KthLargest class:

#     KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
#     int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.


import heapq
from typing import List
import unittest

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        if self.k < len(self.nums):
            heapq.heappop(self.nums)
        return self.nums[0]


# Your KthLargest object will be instantiated and called as such:
obj = KthLargest(3, [4, 5, 8, 2])
assert obj.add(3) == 4
assert obj.add(5) == 5
assert obj.add(10) == 5
assert obj.add(9) == 8
assert obj.add(4) == 8