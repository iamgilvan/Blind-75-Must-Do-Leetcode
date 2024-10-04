import unittest

#TC O(V + E), #EC O(V + E)  V = numCourses E = prerequisites
def graph_valid_tree(n, edges):
    if not n: return True
    visited = set()
    graph = {i: [] for i in range(n)}
    # build the graph
    for n1, n2 in edges:
        graph[n1].append(n2)
        graph[n2].append(n1)

    def dfs(node, prev):
        if node in visited:
            return False
        visited.add(node)
        for node_adj in graph[node]:
            if node_adj == prev: continue
            if not dfs(node_adj, node): return False

        return True
    return dfs(0, -1) and n == len(visited)
class Test(unittest.TestCase):
    test_cases = [
        (5, [[0,1], [0,2], [0,3], [1,4]], True),
    ]
    functions = [graph_valid_tree]
    def test_graph_valid_tree(self):
        for function in self.functions:
            for n, arr, expected in self.test_cases:
                result = function(n, arr)
                assert result == expected

if __name__ == '__main__':
    unittest.main()