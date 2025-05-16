from typing import List
import unittest

# Given an array of integers, find the nearest smaller number for every element such that the smaller element is on the left side.

# Time complexity O(n^2) : Space Complexity O(1)
def prev_smaller(arr) -> List[int]:
    result = [-1]
    for i in range(1, len(arr)):
        for j in range(i - 1, -1, -1):
            if arr[j] < arr[i]:
                result.append(arr[j])
                break
        else:
            result.append(-1)
    return result

# Time complexity O(n) : Space Complexity O(n)
def prev_smaller_stack(arr) -> List[int]:
    result = []
    stack = []
    for i in range(len(arr)):
        while stack and stack[-1] >= arr[i]:
            stack.pop()
        if not stack:
            result.append(-1)
        else:
            result.append(stack[-1])
        stack.append(arr[i])
    return result


class Test(unittest.TestCase):
    test_cases = [
        ([1, 6, 2], [-1, 1, 1]),
        ([1, 5, 0, 3, 4, 5], [-1, 1, -1, 0, 3, 4]),
        ([9, 6, 10, 9, 5], [-1, -1, 6, 6, -1])
    ]
    functions = [prev_smaller, prev_smaller_stack]
    def test_prev_smaller(self):
        for function in self.functions:
            for s, expected in self.test_cases:
                result = function(s)
                assert result == expected

if __name__ == '__main__':
    unittest.main()