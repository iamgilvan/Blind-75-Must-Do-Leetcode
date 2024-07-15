import math
import unittest

# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

# Return the minimum integer k such that she can eat all the bananas within h hours.

#TC O(log(max(p))p)
#TS O(1)
def minEatingSpeed(piles, h):
    left, right = 1, max(piles)
    result = right
    while left <= right:
        k = (left + right) // 2
        hours = 0
        for p in piles:
            hours += math.ceil(p/ k)
        if hours <= h:
            result = min(result, k)
            right = k - 1
        else:
            left = k + 1
    return result

#TC O(max(p)p)
#TS O(1)
def minEatingSpeed_brute_force(piles, h):
    max_value = max(piles)
    result = max_value
    for k in range(1, max_value):
        hours = 0
        for p in piles:
            hours += math.ceil(p/ k)
        if hours <= h:
            result = min(result, k)
    return result

class Test(unittest.TestCase):
    test_cases = [
        ([3,6,7,11], 8, 4),
        ([30,11,23,4,20], 5, 30),
        ([30,11,23,4,20], 6, 23)
    ]
    functions = [minEatingSpeed,minEatingSpeed_brute_force]
    def test_koko_eating_bananas(self):
        for function in self.functions:
            for piles,h, expected in self.test_cases:
                result = function(piles, h)
                assert result == expected

if __name__ == '__main__':
    unittest.main()