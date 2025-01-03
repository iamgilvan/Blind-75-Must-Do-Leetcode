import heapq
from typing import List
import unittest

# Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), find the minimum number of days required to schedule all meetings without any conflicts.

#Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

#TC O(nlogn)
def canAttendMeetings(intervals: List[Interval]) -> bool:
    intervals.sort(key = lambda i : i.start)
    min_heap = []
    for i in intervals:
        if min_heap and min_heap[0] <= i.start:
            heapq.heappop(min_heap)
        heapq.heappush(min_heap, i.end)
    return len(min_heap)

class Test(unittest.TestCase):
    test_cases = [
        ([(0,40),(5,10),(15,20)], 2),
        ([(5,9)], 1),
    ]
    functions = [canAttendMeetings]
    def test_metting_room_ii(self):
        for function in self.functions:
            for intervals_list, expected in self.test_cases:
                intervals = [Interval(s, e) for s, e in intervals_list]
                result = function(intervals)
                assert result == expected

if __name__ == '__main__':
    unittest.main()