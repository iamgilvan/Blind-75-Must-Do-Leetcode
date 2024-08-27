from collections import Counter
import heapq
import unittest

# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

# The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

# You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).
#TC O(nlogn)
def k_Closest_Point_To_Origin(points, k):
    heapMin = []
    for x, y in points:
        dist = (x **2) + (y **2)
        heapq.heappush(heapMin,[dist, x, y])
    heapq.heapify(heapMin)
    res = []
    for _ in range(k):
        dist, x, y = heapq.heappop(heapMin)
        res.append([ x, y])
    return res

class Test(unittest.TestCase):
    test_cases = [
        ([[1,3],[-2,2]], 1, [[-2,2]]),
        ([[3,3],[5,-1],[-2,4]], 2, [[3,3],[-2,4]]),
    ]
    functions = [k_Closest_Point_To_Origin]
    def test_k_Closest_Point_To_Origin(self):
        for function in self.functions:
            for points, k, expected in self.test_cases:
                result = function(points, k)
                assert result == expected

if __name__ == '__main__':
    unittest.main()