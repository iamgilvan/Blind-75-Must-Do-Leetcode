import unittest
# In this problem, a tree is an undirected graph that is connected and has no cycles.

# You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

# Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.
#TC O(n), #EC O(n) 
def redundant_connection(edges):
    n = len(edges) + 1
    par = [i for i in range(n)]
    rank = [1] * n
    def find(node):
        if par[node] != node:
            par[node] = find(par[node])  # Path compression
        return par[node]
    def union(n1, n2):
        p1, p2 = find(n1), find(n2)
        if p1 == p2:
            return False
        if rank[p2] > rank[p1]:
            par[p1] = p2
            rank[p2] += rank[p1]
        else:
            par[p2] = p1
            rank[p1] += rank[p2]
        return True
    for n1, n2 in edges:
        if not union(n1, n2):
                    return [n1, n2]
class Test(unittest.TestCase):
    test_cases = [
        ([[1,2],[1,3],[2,3]], [2,3]),
        ([[1,2],[2,3],[3,4],[1,4],[1,5]], [1,4])
    ]
    functions = [redundant_connection]
    def test_redundant_connection(self):
        for function in self.functions:
            for arr, expected in self.test_cases:
                result = function(arr)
                assert result == expected

if __name__ == '__main__':
    unittest.main()