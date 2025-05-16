from typing import List
import unittest

# Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

# Time complexity O(n^2) : Space Complexity O(1)
def largest_rectangle_area(heights) -> int:

    n = len(heights)
    maxArea = 0

    for i in range(n):
        height = heights[i]
        rightMost = i + 1
        while rightMost < n and heights[rightMost] >= height:
            rightMost += 1

        leftMost = i
        while leftMost >= 0 and heights[leftMost] >= height:
            leftMost -= 1

        rightMost -= 1
        leftMost += 1
        maxArea = max(maxArea, height * (rightMost - leftMost + 1))
    return maxArea

# Time complexity O(n) : Space Complexity O(n)
def largest_rectangle_area_stack(heights: List[int]) -> int:
    maxArea = 0
    stack = []  # pair: (index, height)
    for i, h in enumerate(heights):
        start = i
        while stack and stack[-1][1] > h:
            index, height = stack.pop()
            maxArea = max(maxArea, height * (i - index))
            start = index
        stack.append((start, h))
    for i, h in stack:
        maxArea = max(maxArea, h * (len(heights) - i))
    return maxArea

class Test(unittest.TestCase):
    test_cases = [
        ([7,1,7,2,2,4], 8),
        ([1,3,7], 7),
        ([2,1,5,6,2,3], 10),
        ([2,4], 4)
    ]
    functions = [largest_rectangle_area, largest_rectangle_area_stack]
    def test_largest_rectangle_area(self):
        for function in self.functions:
            for s, expected in self.test_cases:
                result = function(s)
                assert result == expected

if __name__ == '__main__':
    unittest.main()