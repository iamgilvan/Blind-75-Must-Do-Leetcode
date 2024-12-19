from typing import List
import unittest

# Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), determine if a person could add all meetings to their schedule without any conflicts.


#Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

#TC O(nlogn)
def canAttendMeetings(intervals: List[Interval]) -> bool:
    intervals.sort(key = lambda i : i.start)
    curr_metting = intervals[0]
    for i in range(1, len(intervals)):
        if intervals[i].start < curr_metting.end:
            return False
    return True

class Test(unittest.TestCase):
    test_cases = [
        ([(0,30),(5,10),(15,20)], False),
        ([(5,8),(9,15)], True),
    ]
    functions = [canAttendMeetings]
    def test_metting_room(self):
        for function in self.functions:
            for intervals_list, expected in self.test_cases:
                intervals = [Interval(s, e) for s, e in intervals_list]
                result = function(intervals)
                assert result == expected

if __name__ == '__main__':
    unittest.main()