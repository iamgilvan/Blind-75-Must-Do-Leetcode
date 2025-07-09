from collections import defaultdict

# A k-booking happens when k events have some non-empty intersection (i.e., there is some time that is common to all k events.)

# You are given some events [startTime, endTime), after each given event, return an integer k representing the maximum k-booking between all the previous events.

# Implement the MyCalendarThree class:

# MyCalendarThree() Initializes the object.
# int book(int startTime, int endTime) Returns an integer k representing the largest integer such that there exists a k-booking in the calendar.

#Time complexity O(n log n) : Space complexity O(n)
class MyCalendarThree:

    def __init__(self):
        self.timeline = defaultdict(int)
        self.max_overlap = 0

    def book(self, start: int, end: int) -> int:
        self.timeline[start] += 1
        self.timeline[end] -= 1

        # Simula a linha do tempo
        current_overlap = 0
        for time in sorted(self.timeline):
            current_overlap += self.timeline[time]
            self.max_overlap = max(self.max_overlap, current_overlap)

        return self.max_overlap

calendar = MyCalendarThree()
print(calendar.book(10, 20))  # retorna 1
print(calendar.book(50, 60))  # retorna 1
print(calendar.book(10, 40))  # retorna 2
print(calendar.book(5, 15))  # retorna 3
print(calendar.book(5, 10))  # retorna 3
print(calendar.book(25, 55))  # retorna 3
