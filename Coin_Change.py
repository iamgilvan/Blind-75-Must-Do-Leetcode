import unittest

#TC O(amount * n)
#TS O(1)
def coinChange(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1


class Test(unittest.TestCase):
    test_cases = [
        ([1,2,5], 11, 3),
        ([2], 3, -1),
        ([1], 0, 0)
    ]
    functions = [coinChange]
    def test_coin_change(self):
        for function in self.functions:
            for arr, amount, expected in self.test_cases:
                result = function(arr, amount)
                assert result == expected

if __name__ == '__main__':
    unittest.main()