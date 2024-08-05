
# First, we need a Node class to represent each element in the linked list.
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Now, let's implement the Queue class using this Node class. 
# The Queue class will manage the head (front of the queue) and tail (end of the queue) pointers.

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            # If the queue is empty, both head and tail point to the new node
            self.head = self.tail = new_node
        else:
            # Attach the new node to the 'next' of the tail and move the tail to the new node
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        dequeued_value = self.head.value
        self.head = self.head.next
        self.size -= 1
        if self.is_empty():
            # If the queue is empty after dequeue, set tail to None
            self.tail = None
        return dequeued_value

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self.head.value

    def __len__(self):
        return self.size

# Create a queue
queue = Queue()

# Enqueue items
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

# Dequeue items
print(queue.dequeue())  # Output: 1
print(queue.dequeue())  # Output: 2

# Peek at the front item
print(queue.peek())  # Output: 3

# Check the length
print(len(queue))  # Output: 1
