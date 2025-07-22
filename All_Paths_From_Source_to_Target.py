import collections
from typing import List
import unittest

# Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.

# The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).

# TC: O(2^n * n)
# MC: O(2^n * n)
def all_paths_source_target(graph: List[List[int]]) -> List[List[int]]:
    graph_map = collections.defaultdict(list)
    n = len(graph)
    def dfs(index):
        if index in graph_map:
            return graph_map[index]
        if index == n - 1:
            return [[n-1]]
        result = []
        for node in graph[index]:
            res = dfs(node)
            for i in res:
                result.append([index] + i)
        graph_map[index] = result
        return result
    dfs(0)
    return graph_map[0]

class Test(unittest.TestCase):
    test_cases = [
        ([[1,2],[3],[3],[]], [[0,1,3],[0,2,3]]),
        ([[4,3,1],[3,2,4],[3],[4],[]], [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]),
    ]
    functions = [all_paths_source_target]
    def test_all_paths_source_target(self):
        for function in self.functions:
            for graph, expected in self.test_cases:
                result = function(graph)
                assert result == expected

if __name__ == '__main__':
    unittest.main()