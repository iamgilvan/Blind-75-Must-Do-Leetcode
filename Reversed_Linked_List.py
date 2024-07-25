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
    # TC: O(n)
    # MC: O(n)
    def reverseList_ii(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []

        def backtrack(node):
            if not node:
                return
            stack.append(node)
            backtrack(node.next)
        backtrack(head)

        if not stack:
            return head
        
        new_head = stack.pop()
        node = new_head
        while stack:
            cur_node = stack.pop()
            node.next = cur_node
            node = node.next
        node.next = None
        return new_head
    
    # TC: O(n)
    # MC: O(1)
    def reverseList_ii(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr, prev = head, None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev