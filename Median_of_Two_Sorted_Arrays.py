import unittest
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).
#O(log min(n+m))
def median_of_two_sorted_arrays(nums1, nums2):
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2  # A
            j = half - i - 2  # B

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            # partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if total % 2:
                    return min(Aright, Bright)
                # even
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1

class Test(unittest.TestCase):
    test_cases = [
        ([1,3], [2], 2.0),
        ([1,2], [3,4], 2.5),
    ]
    functions = [median_of_two_sorted_arrays]
    def test_median_of_two_sorted_arrays(self):
        for function in self.functions:
            for nums1, nums2, expected in self.test_cases:
                result = function(nums1, nums2)
                assert result == expected

if __name__ == '__main__':
    unittest.main()