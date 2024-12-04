import unittest

# There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

# You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

# Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique.

#TC O(n)
#TS O(1)
def can_complete_circuit(gas, cost) -> int:
    if sum(gas) < sum(cost):
        return -1
    total = 0
    start = 0
    for i in range(len(gas)):
        total += (gas[i] - cost[i])
        if total < 0:
            total = 0
            start = i + 1
    return start

class Test(unittest.TestCase):
    test_cases = [
        ([1,2,3,4,5], [3,4,5,1,2], 3),
        ([2,3,4], [3,4,3], -1)
    ]
    functions = [can_complete_circuit]
    def test_can_complete_circuit(self):
        for function in self.functions:
            for s, p, expected in self.test_cases:
                result = function(s, p)
                assert result == expected

if __name__ == '__main__':
    unittest.main()