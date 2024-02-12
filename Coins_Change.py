import unittest

#TC:  O(amount * n),
def coins_change(coins, amount):
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
        ([2],3, -1),
        ([1], 0, 0),
    ]
    functions = [coins_change]
    def test_combination_sum(self):
        for function in self.functions:
            for coins, amount, expected in self.test_cases:
                result = function(coins, amount)
                assert result == expected

if __name__ == '__main__':
    unittest.main()