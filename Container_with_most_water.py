import unittest

# Time Complexity: O(N), Space Complexity: O(1)
def container_with_most_water(arr):
    start, end = 0, len(arr) -1
    max_container = 0
    while start < end:
        min_h = min(arr[start], arr[end])
        distance = end - start
        curr_area = min_h * distance
        max_container = max(max_container, curr_area)
        if arr[start] > arr[end]:
            end -= 1
        else:
            start += 1
    return max_container

class Test(unittest.TestCase):
    test_cases = [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([1, 1], 1),
    ]
    functions = [container_with_most_water]
    def test_container_with_most_water(self):
        for function in self.functions:
            for arr, expected in self.test_cases:
                result = function(arr)
                assert result == expected

if __name__ == '__main__':
    unittest.main()