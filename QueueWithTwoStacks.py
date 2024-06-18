class QueueWithTwoStacks:
    def __init__(self):
        self.enqueue_stack = []
        self.dequeue_stack = []

    def transfer_elements(self):
        while self.enqueue_stack:
            self.dequeue_stack.append(self.enqueue_stack.pop())

    def enqueue(self, x):
        self.enqueue_stack.append(x)

    def dequeue(self):
        if not self.dequeue_stack:
            self.transfer_elements()
        return self.dequeue_stack.pop()

    def peek(self):
        if not self.dequeue_stack:
            self.transfer_elements()
        return self.dequeue_stack[-1]

# Read number of queries
q = int(input())

# Create a queue
queue = QueueWithTwoStacks()

# Process each query
for _ in range(q):
    query = input().split()
    query_type = int(query[0])

    if query_type == 1:
        # Enqueue operation
        x = int(query[1])
        queue.enqueue(x)
    elif query_type == 2:
        # Dequeue operation
        queue.dequeue()
    elif query_type == 3:
        # Print operation
        print(queue.peek())