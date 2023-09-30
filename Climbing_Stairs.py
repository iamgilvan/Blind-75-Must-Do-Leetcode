import unittest

# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# Example 2:

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step


# TC O(2^n) : SC O(n)
def climbing_stairs_recursive(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    return climbing_stairs_recursive(n - 1) + climbing_stairs_recursive(n - 2)

# TC O(n) : SC O(n)
def climbing_stairs(n):
    ways = [0] * (n + 1)
    ways[0] = 1
    ways[1] = 1

    for i in range(2, n + 1):
        ways[i] = ways[i - 1] + ways[i - 2]
    return ways[n]
class Test(unittest.TestCase):
    test_cases = [
        (2, 2),
        (3, 3)
    ]
    functions = [climbing_stairs, climbing_stairs_recursive]
    def test_climbing_stairs(self):
        for function in self.functions:
            for n, expected in self.test_cases:
                result = function(n)
                assert result == expected

if __name__ == '__main__':
    unittest.main()