from typing import Counter, List
import unittest

# Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.

# Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.

#time complexity O(n log n) : space complexity O(n)
def isNStraightHand(hand, groupSize):
    if len(hand) % groupSize:
        return False
    count = Counter(hand)
    hand.sort()
    for num in hand:
        if count[num]:
            for i in range(num, num + groupSize):
                if not count[i]:
                    return False
                count[i] -= 1
    return True

#time complexity O(N) : space complexity O(N)
def isNStraightHand_ii(hand: List[int], groupSize: int) -> bool:
    if len(hand) % groupSize != 0:
        return False
    count = Counter(hand)
    for num in hand:
        start = num
        while count[start - 1]:
            start -= 1
        while start <= num:
            while count[start]:
                for i in range(start, start + groupSize):
                    if not count[i]:
                        return False
                    count[i] -= 1
            start += 1
    return True

class Test(unittest.TestCase):
    test_cases = [
        ([1,2,3,6,2,3,4,7,8], 3, True),
        ([1,2,3,4,5], 4, False),
    ]
    functions = [isNStraightHand, isNStraightHand_ii]
    def test_is_n_straight_hand(self):
        for function in self.functions:
            for arr, s, expected in self.test_cases:
                result = function(arr, s)
                assert result == expected

if __name__ == '__main__':
    unittest.main()