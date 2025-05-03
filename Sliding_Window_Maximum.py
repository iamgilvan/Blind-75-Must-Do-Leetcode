import collections
import heapq
import unittest

# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

# Return the max sliding window.
#TC O(n)
#TS O(1)
def max_sliding_window(arr, k):
    result = []
    l, r = 0, k
    while r <= len(arr):
        partial_arr = arr[l:r]
        max_n = max(partial_arr)
        result.append(max_n)
        l += 1
        r += 1
    return result

#TC O(n)
#TS O(n)
def max_sliding_window_q(arr, k):
    result = []
    heap = collections.deque()
    l = r = 0
    while r < len(arr):
        while heap and arr[heap[-1]] < arr[r]:
            heap.pop()
        heap.append(r)
        if l > heap[0]:
            heap.popleft()

        if (r + 1) >= k:
            l += 1
            result.append(arr[heap[0]])
        r +=1
    return result

class Test(unittest.TestCase):
    test_cases = [
        ([1,3,-1,-3,5,3,6,7], 3, [3,3,5,5,6,7]),
        ([1], 1, [1]),
    ]
    functions = [max_sliding_window, max_sliding_window_q]
    def test_max_sliding_window(self):
        for function in self.functions:
            for arr, k, expected in self.test_cases:
                result = function(arr, k)
                assert result == expected

if __name__ == '__main__':
    unittest.main()