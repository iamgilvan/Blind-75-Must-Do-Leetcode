import heapq
import statistics
import unittest


#SC : O(n)
class MedianFinder:

    def __init__(self):
        self.min_heap = []  # Heap para a metade superior
        self.max_heap = []  # Heap para a metade inferior

    #TC : O(log n)
    def addNum(self, num: int) -> None:
        # Insere o número na heap apropriada
        if not self.max_heap or num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)

        # Balanceamento das heaps
        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
    # TC: O(1)
    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2 if self.min_heap else 0.0
        else:
            return -self.max_heap[0]

#SC : O(n)
class MedianFinderBruteForce:

    def __init__(self):
       self.arr=[]

    def addNum(self, num: int) -> None:
        self.arr.append(num)

    def findMedian(self) -> float:
        self.arr.sort()
        return statistics.median(self.arr)

class Test(unittest.TestCase):
    def test_media_finder(self):
        medianFinder = MedianFinder();
        assert medianFinder.addNum(1) == None
        assert medianFinder.addNum(2) == None
        assert medianFinder.findMedian() == 1.5 # (i.e., (1 + 2) / 2)
        assert medianFinder.addNum(3) == None
        assert medianFinder.findMedian() == 2.0
        
        medianFinder = MedianFinderBruteForce();
        assert medianFinder.addNum(1) == None
        assert medianFinder.addNum(2) == None
        assert medianFinder.findMedian() == 1.5 # (i.e., (1 + 2) / 2)
        assert medianFinder.addNum(3) == None
        assert medianFinder.findMedian() == 2.0

if __name__ == '__main__':
    unittest.main()