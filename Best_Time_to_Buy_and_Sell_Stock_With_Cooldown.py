import unittest

# O(n) time
# O(n) space
def best_time_to_buy_and_sell_stock_with_cooldown(prices):
    dp = {}  # key=(i, buying) val=max_profit
    def dfs(i, buying):
        if i >= len(prices):
            return 0
        if (i, buying) in dp:
            return dp[(i, buying)]
        cooldown = dfs(i + 1, buying)
        if buying:
            buy = dfs(i + 1, not buying) - prices[i]
            dp[(i, buying)] = max(buy, cooldown)
        else:
            sell = dfs(i + 2, not buying) + prices[i]
            dp[(i, buying)] = max(sell, cooldown)
        return dp[(i, buying)]
    return dfs(0, True)

# O(n) time
# O(1) space
def best_time_to_buy_and_sell_stock_with_cooldown_(prices):
        n = len(prices)
        dp1_buy, dp1_sell = 0, 0
        dp2_buy = 0

        for i in range(n - 1, -1, -1):
            dp_buy = max(dp1_sell - prices[i], dp1_buy)
            dp_sell = max(dp2_buy + prices[i], dp1_sell)
            dp2_buy, dp1_sell = dp1_buy, dp1_sell
            dp1_buy, dp1_sell = dp_buy, dp_sell

        return dp1_buy
class Test(unittest.TestCase):
    test_cases = [
        ([1,2,3,0,2], 3),
        ([1],0),
    ]
    functions = [best_time_to_buy_and_sell_stock_with_cooldown, best_time_to_buy_and_sell_stock_with_cooldown_]
    def test_best_time_to_buy_and_sell_stock_with_cooldown(self):
        for function in self.functions:
            for prices, expected in self.test_cases:
                result = function(prices)
                assert result == expected

if __name__ == '__main__':
    unittest.main()