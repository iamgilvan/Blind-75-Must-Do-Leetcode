import unittest

# O(n) time
# O(1) space
def best_time_to_buy_and_sell_stock(prices):
    if not prices: return 0
    min_price = prices[0]
    max_profit = 0

    for price in prices[1:]:
        if price < min_price:
            min_price = price
        else:
            max_profit = max(max_profit, price - min_price)

    return max_profit

class Test(unittest.TestCase):
    test_cases = [
        ([7,1,5,3,6,4], 5),
        ([7,6,4,3,1],0),
        ([2,4,1], 2)
    ]
    functions = [best_time_to_buy_and_sell_stock]
    def test_two_sum(self):
        for function in self.functions:
            for prices, expected in self.test_cases:
                result = function(prices)
                assert result == expected

if __name__ == '__main__':
    unittest.main()