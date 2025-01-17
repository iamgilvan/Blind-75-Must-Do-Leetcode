from collections import defaultdict
from typing import List

# You are given a stream of points on the X-Y plane. Design an algorithm that:

# Adds new points from the stream into a data structure. Duplicate points are allowed and should be treated as different points.
# Given a query point, counts the number of ways to choose three points from the data structure such that the three points and the query point form an axis-aligned square with positive area.
# An axis-aligned square is a square whose edges are all the same length and are either parallel or perpendicular to the x-axis and y-axis.

# Implement the DetectSquares class:

# DetectSquares() Initializes the object with an empty data structure.
# void add(int[] point) Adds a new point point = [x, y] to the data structure.
# int count(int[] point) Counts the number of ways to form axis-aligned squares with point point = [x, y] as described above.
class DetectSquares:

    def __init__(self):
        # Dictionary to store the count of each point
        self.point_count = defaultdict(int)

    def add(self, point: List[int]) -> None:
        # increment the count for the give point
        self.point_count[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        x, y = point
        count_squares = 0

        # iterate through all points in the dictionary 
        for (px, py), cnt in list(self.point_count.items()):
            if px == x and py != y:
                # calc the side length of the square
                side_length = abs(py - y)

                # check for the other two corners of the square
                count_squares += cnt * self.point_count[(x + side_length, y)] * self.point_count[(x + side_length, py)]
                count_squares += cnt * self.point_count[(x - side_length, y)] * self.point_count[(x - side_length, py)]
        return count_squares


# Example usage
obj = DetectSquares()
assert obj.add([3,10]) == None
assert obj.add([11,2]) == None
assert obj.add([3,2]) == None
assert obj.count([11,10]) == 1
assert obj.count([14,8]) == 0
assert obj.add([11,2]) == None
assert obj.count([11,10]) == 2