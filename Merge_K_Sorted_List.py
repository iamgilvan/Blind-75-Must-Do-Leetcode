import heapq
from typing import Optional
import unittest

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#O(n * k * log(k))
def mergeKSortedList(nList):
    nList = [x for x in nList if x]
    if len(nList) == 0:
        return None

    if len(nList) == 1:
        return nList[0]

    if len(nList) == 2:
        return mergeTwoList(nList[0], nList[1])

    temp_l = mergeTwoList(nList[0], nList[1])
    for i in range(2, len(nList)):
        temp_l = mergeTwoList(temp_l, nList[i])
    return temp_l

def mergeTwoList(l1, l2):
    dummy = ListNode(0)
    current = dummy
    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    if l1:
        current.next = l1
    if l2:
        current.next = l2
    return dummy.next

#O(NLogK)
def merge_k_list(nList)-> Optional[ListNode]:
    if len(nList) == 0: return None
    heap = []
    for i in range(len(nList)):
        if not nList[i]: continue
        heapq.heappush(heap, (nList[i].val, i, nList[i]))
    if len(heap) == 0: return None
    dummy = ListNode(0)
    d_node = dummy
    while heap:
        val, j , node = heapq.heappop(heap)
        d_node.next = node
        d_node = d_node.next
        if node.next:
            heapq.heappush(heap, (node.next.val, j, node.next))
    return dummy.next

class Test(unittest.TestCase):
    test_cases = [
        ([[1,4,5],[1,3,4],[2,6]], [1,1,2,3,4,4,5,6]),
        ([], []),
        ([[]], []),
        ([[],[]], [])
    ]
    functions = [mergeKSortedList, merge_k_list]
    def test_merge_k_sorted_list(self):
        for function in self.functions:
            for arrl, expected in self.test_cases:
                my_arr = []
                for arr in arrl:
                    dummy = ListNode(0)
                    tail = dummy
                    for i in arr:
                        tail.next = ListNode(i)
                        tail = tail.next
                    my_arr.append(dummy.next)
                result = function(my_arr)
                values = []
                while result:
                    values.append(result.val)
                    result = result.next
                assert values == expected

if __name__ == '__main__':
    unittest.main()