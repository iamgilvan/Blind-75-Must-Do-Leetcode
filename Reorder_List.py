# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln

# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

# TC: O(n)
# MC: O(n)
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        # Passo 1: Encontrar o ponto médio
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Passo 2: Inverter a Segunda Metade e Armazenar em uma Estrutura Auxiliar
        stack = []
        current = slow.next
        while current:
            stack.append(current)
            current = current.next
        slow.next = None  # Divide a lista em duas partes

        # Passo 3: Interleaving (Entrelaçamento) das Duas Metades
        current = head
        while stack:
            temp = current.next
            current.next = stack.pop()
            current.next.next = temp
            current = temp