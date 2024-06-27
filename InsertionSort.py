def insertionSort(arr):
    # Write your code here
    shift = 0
    for i in range(1, len(arr)):
        actualN = arr[i]
        prevN = i - 1
        while prevN >= 0 and actualN < arr[prevN]:
            arr[prevN + 1] = arr[prevN]
            shift += 1
            prevN -=1
        arr[prevN+1] = actualN
    return shift

    
    # Simple algorithm. 
    # The idea is just to store the deleted values in a set or dict. 
    # And then when it comes to print the minimum, check if the current heap minimum has been deleted or not. 
    # If it has, deleted it from the heap and from the deleted set. If not, then, that's the min. 
    # import heapq

    # li = []
    # heapq.heapify(li)
    # Q = int(input())
    # deleted = set()
    # for _ in range(Q):
    #     query = input().split()
    #     if query[0] == "1":
    #         heapq.heappush(li, int(query[1]))
    #     if query[0] == "2":
    #         deleted.add(int(query[1]))
    #     if query[0] == "3":
    #         min_test = heapq.heappop(li)
    #         while min_test in deleted:
    #             deleted.remove(min_test)
    #             min_test = heapq.heappop(li)
    #         heapq.heappush(li, min_test)
    #         print(min_test)
    
    class BinarySearchTree:
    def __init__(self):
        self.root = None

#Node is defined as
#self.left (the left child of the node)
#self.right (the right child of the node)
#self.info (the value of the node)

    def insert(self, val):
        #Enter you code here.
        new_node = Node(val)
        if self.root is None:
            self.root = new_node
            return self.root
        curr = self.root
        while True:
            if new_node.info < curr.info:
                if curr.left is None:
                    curr.left = new_node
                    break
                else:
                    curr = curr.left
            elif new_node.info > curr.info:
                if curr.right is None:
                    curr.right = new_node
                    break
                else:
                    curr = curr.right
        return self.root
    # O(log n)
    def height(root):
        if root is None:
            return -1
        else:
            return 1 + max(self.height(root.left), self.height(root.right))
        
        
        
from collections import defaultdict, deque


def bfs(n, m, edges, s):
    # Write your code here
    # Create graph representation as adjacency list
    graph = defaultdict(set)
    for start, end in edges:
        graph[start].add(end)
        graph[end].add(start)
    
    # Use hash table to store distances
    distances = {}
    
    # Use deque as a queue
    q = deque([(s, 0)])
    while q:
        curr, dist = q.popleft()
        if curr in distances:
            continue
        distances[curr] = dist
        # push all neighbors to queue along with the distance
        q.extend([(n, dist+6) for n in graph[curr]])
    
    result = []
    for i in range(1, n+1):
        if i == s:
            continue
        result.append(distances.get(i, -1))
    return result

def quickestWayUp(ladders, snakes):
    # Write your code here
    graph1 = dict()
    for u, v in ladders:
        graph1[u] = v
    graph2 = dict()
    for u, v in snakes:
        graph2[u] = v
    q = deque()
    visit = set()
    q.append([1, 0])
    while(q): 
        square, moves = q.popleft()
        for i in range(1, 7):
            next_square = square + i
            if graph1.get(next_square):
                next_square = graph1.get(next_square)
            elif graph2.get(next_square):
                next_square = graph2.get(next_square)
            
            if next_square == 100:
                return moves + 1
            if next_square not in visit:
                visit.add(next_square)
                q.append([next_square, moves+1])
            
    return -1


def Fibonacci(n):
 
    # Check if input is 0 then it will
    # print incorrect input
    if n < 0:
        print("Incorrect input")
 
    # Check if n is 0
    # then it will return 0
    elif n == 0:
        return 0
 
    # Check if n is 1,2
    # it will return 1
    elif n == 1 or n == 2:
        return 1
 
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)