import heapq
import unittest

# You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

# The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

# Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

#TC O(N^2)
def min_cost_connect_points(points):
    n = len(points)

    adj = { i:[] for i in range(n)}
    for i in range(n):
        x1,y1 = points[i]
        for j in range(i + 1, n):
            x2,y2 = points[j]
            dist = abs(x1 - x2) + abs(y1 - y2)
            adj[i].append([dist, j])
            adj[j].append([dist, i])
    # Prim's
    res = 0
    visit = set()
    minH = [[0,0]]
    while len(visit) < n:
        cost, i = heapq.heappop(minH)
        if i in visit: continue
        res += cost
        visit.add(i)
        for neiCost, nei in adj[i]:
            if nei not in visit:
                heapq.heappush(minH, [neiCost, nei])
    return res

class Test(unittest.TestCase):
    test_cases = [
        ([[0,0],[2,2],[3,10],[5,2],[7,0]], 20),
        ([[3,12],[-2,5],[-4,1]], 18),
    ]
    functions = [min_cost_connect_points]
    def test_min_cost_connect_points(self):
        for function in self.functions:
            for arr, expected in self.test_cases:
                result = function(arr)
                assert result == expected

if __name__ == '__main__':
    unittest.main()