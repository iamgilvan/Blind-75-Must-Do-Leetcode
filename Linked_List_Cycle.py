# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # O(n) time
    # O(n) space
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = []

        while head:

            if head in visited:
                return True

            visited.append(head)
            head = head.next
        return False
    # O(n) time
    # O(1) space
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False

        slow = head
        fast = head.next

        while slow != fast:
            if not fast or not fast.next:
                return False

            slow = slow.next
            fast = fast.next.next

        return True