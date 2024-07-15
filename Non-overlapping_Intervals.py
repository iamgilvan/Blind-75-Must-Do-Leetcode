import unittest

# Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

#TC O(nlogn)
def eraseOverlapIntervals(intervals):
    intervals.sort()
    res = 0
    prev = intervals[0][1]
    for i in range(1, len(intervals)):
        s, e = intervals[i][0], intervals[i][1]
        if s >= prev:
            prev = e
        else:
            res += 1
            prev = min(e, prev)
    return res

class Test(unittest.TestCase):
    test_cases = [
        ([[1,2],[2,3],[3,4],[1,3]], 1),
        ([[1,2],[1,2],[1,2]], 2),
        ([[1,2],[2,3]], 0),
        ([[1,100],[11,22],[1,11],[2,12]], 2),
        ([[0,1],[3,4],[1,2]], 0)
    ]
    functions = [eraseOverlapIntervals]
    def test_non_overlapping(self):
        for function in self.functions:
            for intervals, expected in self.test_cases:
                result = function(intervals)
                assert result == expected

if __name__ == '__main__':
    unittest.main()