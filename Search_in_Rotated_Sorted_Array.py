import unittest

def search_in_rotate_sorted_array(arr, target):
    if not arr:
        return -1
    idx_rotation = find_rotation_point(arr)
    if arr[idx_rotation] == target:
        return idx_rotation
    elif target in arr[idx_rotation:]:
        right = len(arr) - 1
        left = idx_rotation
    else:
        right = idx_rotation
        left = 0

    while left <= right:
        middle =  left + (right - left) // 2

        if arr[middle] == target:
            return middle

        if arr[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return -1

def find_rotation_point(arr):
    '''Binary search to find the array position was altered'''
    left = 0
    right = len(arr) - 1

    while left < right:
        middle = left + (right - left) // 2

        if arr[middle] > arr[right]:
            left = middle + 1
        else:
            right = middle

    return left

class Test(unittest.TestCase):
    test_cases = [
        ([4,5,6,7,0,1,2], 0, 4),
        ([4,5,6,7,0,1,2], 7, 3),
        ([4,5,6,7,0,1,2], 3, -1),
        ([1], 0, -1),
    ]
    functions = [search_in_rotate_sorted_array]
    def test_search_in_rotate_sorted_array(self):
        for function in self.functions:
            for arr, target, expected in self.test_cases:
                result = function(arr, target)
                assert result == expected

if __name__ == '__main__':
    unittest.main()