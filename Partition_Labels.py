from typing import List
import unittest

# You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

# Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

# Return a list of integers representing the size of these parts.

# Time complexity O(n) : Space Complexity O(1)
def partition_label(s) -> List[int]:
    partition = {}
    res = []
    for i, v in enumerate(s):
        partition[v] = i

    size, end = 0, 0
    for i in range(len(s)):
        size += 1
        end = max(end, partition[s[i]])
        if i == end:
            res.append(size)
            size = 0
    return res

class Test(unittest.TestCase):
    test_cases = [
        ("ababcbacadefegdehijhklij", [9,7,8]),
        ("eccbbbbdec", [10]),
    ]
    functions = [partition_label]
    def test_partition_label(self):
        for function in self.functions:
            for s, expected in self.test_cases:
                result = function(s)
                assert result == expected

if __name__ == '__main__':
    unittest.main()