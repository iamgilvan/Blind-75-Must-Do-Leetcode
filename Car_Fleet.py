import unittest

#TC O(n)
#TS O(n)
def car_fleet(target, position, speed):
    pairs = [[p,s] for p,s in zip(position, speed)]
    stack = []
    for p,s in sorted(pairs)[::-1]: # reverse sorted order
        stack.append((target - p) / s)
        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()
    return len(stack)
#TC O(n)
#TS O(n)
def car_fleet_no_stack(target, position, speed):
    pairs = [(position[i], speed[i]) for i in range(len(position))]
    fleets = curtime = 0  # a car's position is always < than target at the start, so it's fine to start curtime at 0 (no fleet will be at target at time 0)
    for dist, speed in sorted(pairs, reverse=True):
        destination_time = (target - dist)/speed
        if curtime < destination_time:
            fleets += 1
            curtime = destination_time
    return fleets

class Test(unittest.TestCase):
    test_cases = [
        (12, [10,8,0,5,3], [2,4,1,1,3], 3),
        (10, [3], [3], 1),
        (100, [0,2,4], [4,2,1], 1)
    ]
    functions = [car_fleet, car_fleet_no_stack]
    def test_car_fleet(self):
        for function in self.functions:
            for t, p, s, expected in self.test_cases:
                result = function(t,p,s)
                assert result == expected

if __name__ == '__main__':
    unittest.main()