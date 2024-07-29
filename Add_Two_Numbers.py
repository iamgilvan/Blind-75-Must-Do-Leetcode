import unittest
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#TC O(max(m,n))
#TS O(max(m,n))
def addTwoNumbers(list1, list2):
    dummy = ListNode(0)
    tail = dummy
    stack1 = []
    stack2 = []
    while list1:
        stack1.append(str(list1.val))
        list1 = list1.next

    while list2:
        stack2.append(str(list2.val))
        list2 = list2.next
    stack1.reverse()
    stack2.reverse()
    total = int("".join(stack1)) + int("".join(stack2))

    for c in str(total)[::-1]:
        tail.next = ListNode(int(c))
        tail = tail.next

    return dummy.next

#TC O(max(m,n))
#TS O(max(m,n))
def add_two_numbers(list1, list2):
    dummy = ListNode(0)
    tail = dummy
    carry = 0
    while list1 or list2 or carry:
        val1 = list1.val if list1 else 0
        val2 = list2.val if list2 else 0

        val = val1 + val2 + carry
        carry = val // 10
        val = val % 10

        tail.next = ListNode(val)
        tail = tail.next

        list1 = list1.next if list1 else None
        list2 = list2.next if list2 else None
    return dummy.next

class Test(unittest.TestCase):
    test_cases = [
        (ListNode(2,ListNode(4,ListNode(3))), ListNode(5,ListNode(6,ListNode(4))), ListNode(7, ListNode(0,ListNode(8)))),
        (ListNode(0), ListNode(0), ListNode(0)),
        (
            ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9))))))),
                  ListNode(9,ListNode(9,ListNode(9,ListNode(9)))),
                  ListNode(8,ListNode(9,ListNode(9,ListNode(9,ListNode(0,ListNode(0,ListNode(0,ListNode(1))))))))),
    ]
    functions = [addTwoNumbers, add_two_numbers]
    def test_add_two_numbers(self):
        for function in self.functions:
            for list1, list2, expected in self.test_cases:
                result = function(list1, list2)
                while result or expected:
                    if result.val != expected.val:
                        assert False
                    result = result.next
                    expected = expected.next
                assert True

if __name__ == '__main__':
    unittest.main()