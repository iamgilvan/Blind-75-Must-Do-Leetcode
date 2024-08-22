from collections import deque
import heapq
import unittest

# You are given an array of integers stones where stones[i] is the weight of the ith stone.

# We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

#     If x == y, both stones are destroyed, and
#     If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.

# At the end of the game, there is at most one stone left.

# Return the weight of the last remaining stone. If there are no stones left, return 0.

# O(N∗Log(N)) time
# O(h) space
def last_stone_weight(stones):
    if len(stones) == 0:
        return 0
    heapq.heapify(stones)
    while len(stones) > 1:
        curr_stone = heapq.nlargest(2, stones)
        stone_w = curr_stone[0] - curr_stone[1]
        stones = sorted(stones)
        stones = stones[:-2]
        heapq.heappush(stones,stone_w)
    return stones[0]

def last_stone_weight_i(stones):
    stones = [-s for s in stones]
    heapq.heapify(stones)
    while len(stones) > 1:
        first, second = heapq.heappop(stones), heapq.heappop(stones)
        diff = - abs(first-second)
        heapq.heappush(stones, diff)
    return abs(stones[0])

class TestCase(unittest.TestCase):
    def test_last_stone_weight(self):
        assert last_stone_weight([2,7,4,1,8,1]) == 1
        assert last_stone_weight([1]) == 1
        assert last_stone_weight([2,2]) == 0
        assert last_stone_weight([4,6,4,10]) == 4

        assert last_stone_weight_i([2,7,4,1,8,1]) == 1
        assert last_stone_weight_i([1]) == 1
        assert last_stone_weight_i([2,2]) == 0
        assert last_stone_weight_i([4,6,4,10]) == 4

if __name__ == "__main__":
    unittest.main()