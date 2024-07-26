import unittest
# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __len__(self):
            count = 1
            node = self.next
            while node:
                count += 1
                node = node.next
            return count

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

    def __len__(self):
            count = 0
            node = self.head
            while node:
                count += 1
                node = node.next
            return count

# TC: O(n)
# MC: O(1)
def remove_node_n(head , n):
    # obter tamanho da lista
    curr_length = 0
    node = head.head
    while node:
        curr_length += 1
        node = node.next

    idx_to_remove = curr_length - n
    dummy = ListNode(0)
    dummy.next = head.head
    node = dummy
    for _ in range(idx_to_remove):
        node = node.next

    node.next = node.next.next

    return dummy.next

class Test(unittest.TestCase):
    test_cases = [
        ([1,2,3,4,5], 2, [1,2,3,5], 4),
        ([1], 1, [], 0),
        ([1,2], 1, [1], 1),
    ]
    functions = [remove_node_n]
    def test_remove_node_n(self):
        for function in self.functions:
            for arr, target, expected, length in self.test_cases:
                head = LinkedList()
                for i in arr:
                    head.append(i)
                result = function(head, target)
                assert result.__len__() if result else 0 == length

if __name__ == '__main__':
    unittest.main()