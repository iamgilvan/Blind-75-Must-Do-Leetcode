import unittest

# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

# You may assume that you have an infinite number of each kind of coin.


# Time complexity: O(n∗a)
# Space complexity: O(a)

def coins_change(coins, amount):
    dp = [0] * (amount + 1)
    dp[0] = 1
    for i in range(len(coins) - 1, -1, -1):
        for a in range(1, amount + 1):
            dp[a] += dp[a - coins[i]] if coins[i] <= a else 0
    return dp[amount]


# Time complexity: O(2^max(n,am))
# Space complexity: O(max(n,am))
def coins_change_2(coins, amount) -> int:
    coins.sort()
    def dfs(i, a):
        if a == 0:
            return 1
        if i >= len(coins):
            return 0
        res = 0
        if a >= coins[i]:
            res = dfs(i + 1, a)
            res += dfs(i, a - coins[i])
        return res
    return dfs(0, amount)

class Test(unittest.TestCase):
    test_cases = [
        ([1,2,5], 5, 4),
        ([2],3, 0),
        ([10], 10, 1),
    ]
    functions = [coins_change, coins_change_2]
    def test_combination_sum(self):
        for function in self.functions:
            for coins, amount, expected in self.test_cases:
                result = function(coins, amount)
                assert result == expected

if __name__ == '__main__':
    unittest.main()