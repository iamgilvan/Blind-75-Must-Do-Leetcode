import unittest

# You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.

# All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.

#     For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].

# You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.number of unique combinations that sum up to target is less than 150 combinations for the given input.

#TC O(e^2)
#TS O(e)
# where 'e' is the edge number
def reconstruct_itinerary(tickets):
    result = []
    adj = { src : [] for src, dst in tickets}

    for src, dst in tickets:
        adj[src].append(dst)

    for key in adj:
         adj[key].sort()

    def dfs(adj, result, src):
        if src in adj:
            destinations = adj[src][:]
            while destinations:
                dst = destinations[0]
                adj[src].pop(0)
                dfs(adj, result, dst)
                destinations = adj[src][:]
        result.append(src)
    dfs(adj, result, "JFK")
    result.reverse()
    if len(result) != len(tickets) + 1:
            return []
    return result

class Test(unittest.TestCase):
    test_cases = [
        ([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]], ["JFK","MUC","LHR","SFO","SJC"]),
        ([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]], ["JFK","ATL","JFK","SFO","ATL","SFO"]),
    ]
    functions = [reconstruct_itinerary]
    def test_reconstruct_itinerary(self):
        for function in self.functions:
            for arr, expected in self.test_cases:
                result = function(arr)
                assert result == expected

if __name__ == '__main__':
    unittest.main()