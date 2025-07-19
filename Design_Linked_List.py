class LinkedListNode:
    def __init__(self, value, next_node=None, prev_node=None):
        self.value = value
        self.next = next_node
        self.prev = prev_node

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0  # contador de elementos

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.value

    def addAtHead(self, val: int) -> None:
        new_node = LinkedListNode(val, self.head)
        if self.head:
            self.head.prev = new_node
        else:
            self.tail = new_node  # lista vazia
        self.head = new_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        new_node = LinkedListNode(val, None, self.tail)
        if not self.tail:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        if index == 0:
            self.addAtHead(val)
            return
        if index == self.size:
            self.addAtTail(val)
            return

        curr = self.head
        for _ in range(index):
            curr = curr.next

        new_node = LinkedListNode(val, curr, curr.prev)
        if curr.prev:
            curr.prev.next = new_node
        curr.prev = new_node

        if index == 0:
            self.head = new_node

        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        curr = self.head
        for _ in range(index):
            curr = curr.next

        if curr.prev:
            curr.prev.next = curr.next
        else:
            self.head = curr.next

        if curr.next:
            curr.next.prev = curr.prev
        else:
            self.tail = curr.prev

        self.size -= 1

# MyLinkedList myLinkedList = new MyLinkedList();
# myLinkedList.addAtHead(1);
# myLinkedList.addAtTail(3);
# myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
# myLinkedList.get(1);              // return 2
# myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
# myLinkedList.get(1);              // return 3