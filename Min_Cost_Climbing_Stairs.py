import unittest

# You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

# You can either start from the step with index 0, or the step with index 1.

# Return the minimum cost to reach the top of the floor.

# TC O(n) : SC O(1)
def min_cost_climbing_stairs(cost):
    cost.append(0)
    for i in range(len(cost) - 3, -1, -1):
        cost[i] += min(cost[i + 1], cost[i + 2])
    return min(cost[0], cost[1])
class Test(unittest.TestCase):
    test_cases = [
        ([10,15,20], 15),
        ([1,100,1,1,1,100,1,1,100,1], 6)
    ]
    functions = [min_cost_climbing_stairs]
    def test_min_cost_climbing_stairs(self):
        for function in self.functions:
            for n, expected in self.test_cases:
                result = function(n)
                assert result == expected

if __name__ == '__main__':
    unittest.main()