# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        queue = collections.deque()
        node = head
        while node:
            queue.append(node)
            node = node.next
        
        new_head = queue.pop()
        node = new_head
        while queue:
            current_node = queue.pop()
            node.next = current_node
            node = node.next
        node.next = None
        return new_head