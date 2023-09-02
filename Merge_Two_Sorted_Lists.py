import unittest

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node


def mergeTwoList(list1, list2):
    list1 = list1.head
    list2 = list2.head
    dummy = ListNode(0)
    tail = dummy
    while list1 and list2:
        value1 = list1.val
        value2 = list2.val

        if value2 > value1:
            tail.next = ListNode(value1)
            tail = tail.next
            list1 = list1.next
        else:
            tail.next = ListNode(value2)
            tail = tail.next
            list2 = list2.next

    if list1:
         tail.next = list1
    elif list2:
        tail.next = list2
    return dummy.next

class Test(unittest.TestCase):
    test_cases = [
        ([1,2,4], [1,3,4], [1,1,2,3,4,4]),
        ([], [], []),
        ([], [0], [0]),
    ]
    functions = [mergeTwoList]
    def test_two_sum(self):
        for function in self.functions:
            for arr1, arr2, expected in self.test_cases:
                list1 = LinkedList()
                for i in arr1:
                    list1.append(i)
                list2 = LinkedList()
                for i in arr2:
                    list2.append(i)
                result = function(list1, list2)
                values = []
                while result:
                    values.append(result.val)
                    result = result.next
                assert values == expected

if __name__ == '__main__':
    unittest.main()