import unittest

# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

# You may assume that you have an infinite number of each kind of coin.

#TC O(amount * n)
#TS O(amount)
def coinChange(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1

def coinChange2(coins, amount):
    memo = {}

    def dp(amount):
        if amount in memo:
            return memo[amount]
        if amount == 0:
            return 0
        if amount < 0:
            return -1

        min_coins = float('inf')
        for coin in coins:
            subproblem = dp(amount - coin)
            if subproblem == -1:
                continue
            min_coins = min(min_coins, 1 + subproblem)

        memo[amount] = min_coins if min_coins != float('inf') else -1
        return memo[amount]

    return dp(amount)

class Test(unittest.TestCase):
    test_cases = [
        ([1,2,5], 11, 3),
        ([2], 3, -1),
        ([1], 0, 0)
    ]
    functions = [coinChange, coinChange2]
    def test_coin_change(self):
        for function in self.functions:
            for arr, amount, expected in self.test_cases:
                result = function(arr, amount)
                assert result == expected

if __name__ == '__main__':
    unittest.main()