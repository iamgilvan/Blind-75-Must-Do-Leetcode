import unittest

#TC O(V + E), #EC O(V + E)  V = numCourses E = prerequisites
def numbers_of_connected(n, edges):
    par = [i for i in range(n)]
    rank = [1] * n
    def find(node):
        if par[node] != node:
            par[node] = find(par[node])  # Path compression
        return par[node]

    def union(n1, n2):
        p1, p2 = find(n1), find(n2)
        if p1 == p2:
            return 0
        if rank[p2] > rank[p1]:
            par[p1] = p2
            rank[p2] += rank[p1]
        else:
            par[p2] = p1
            rank[p1] += rank[p2]
        return 1

    res = n
    for n1, n2 in edges:
        res -= union(n1, n2)
    return res
class Test(unittest.TestCase):
    test_cases = [
        (5, [[0,1], [1,2], [3,4]], 2),
    ]
    functions = [numbers_of_connected]
    def test_numbers_of_connected(self):
        for function in self.functions:
            for n, arr, expected in self.test_cases:
                result = function(n, arr)
                assert result == expected

if __name__ == '__main__':
    unittest.main()