from collections import Counter
import heapq
import unittest

#TC O(nlogn)
def topKFrequentElements(nums, k):
    frequencies = {}
    for n in nums:
        if n in frequencies:
            frequencies[n] += 1
        else:
            frequencies[n] = 1
    s = sorted(frequencies, key=frequencies.get, reverse=True)
    res = s[:k]
    return res

#TC O(nlogn)
def topK_frequent_elements(nums, k):
    frequencies = Counter(nums)
    s = sorted(frequencies, key=frequencies.get, reverse=True)
    res = s[:k]
    return res

#TC O(nlogk)
def top_k_frequent_elements(nums, k):
    frequencies = Counter(nums)
    heap = []
    for key, freq in frequencies.items():
        if len(heap) < k:
            heapq.heappush(heap, (freq, key))
        else:
            if freq > heap[0][0]:
                heapq.heappop(heap)
                heapq.heappush(heap, (freq, key))
    
    top_k_elements = [item[1] for item in heap]
    
    return top_k_elements
class Test(unittest.TestCase):
    test_cases = [
        ([1,1,1,2,2,3], 2, [1, 2]),
        ([1], 1, [1]),
        ([4,1,-1,2,-1,2,3], 2, [-1, 2])
    ]
    functions = [topKFrequentElements, topK_frequent_elements, top_k_frequent_elements]
    def test_topkfrequentElements(self):
        for function in self.functions:
            for nums, k, expected in self.test_cases:
                result = function(nums, k)
                assert result == expected

if __name__ == '__main__':
    unittest.main()