from collections import defaultdict
import heapq
from typing import List
import unittest

# You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

# We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

# Example 1:

# Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
# Output: 2
# Example 2:

# Input: times = [[1,2,1]], n = 2, k = 1
# Output: 1
# Example 3:

# Input: times = [[1,2,1]], n = 2, k = 2
# Output: -1

#Time complexity O((V + E) log (V)) : Space complexity O(V + E)
def network_delay_time(times: List[List[int]], n: int, k: int) -> int:
    graph = defaultdict(list)
    for u, v, time in times:
        graph[u].append((v, time))

    min_times = {}
    min_heap = [{0, k}] # (distance from source to node, node)

    while min_heap:
        time_k_to_i, i = heapq.heappop(min_heap)
        if i in min_times: continue

        min_times[i] = time_k_to_i
        for nei, nei_time in graph[i]:
            if nei not in min_times:
                heapq.heappush(min_heap, (time_k_to_i + nei_time, nei))
    if len(min_times) == n:
        return max(min_times.values())
    else:
        return -1

class Test(unittest.TestCase):
    test_cases = [
        ([[2,1,1],[2,3,1],[3,4,1]], 4, 2, 2),
        ([[1,2,1]], 2, 1, 1),
        ([[1,2,1]], 2, 2, -1),
    ]
    functions = [network_delay_time]

    def test_network_delay_time(self):
        for function in self.functions:
            for arr, n, k , expected in self.test_cases:
                result = function(arr, n, k)
                assert result == expected

if __name__ == '__main__':
    unittest.main()