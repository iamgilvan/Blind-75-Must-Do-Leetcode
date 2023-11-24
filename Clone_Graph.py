from collections import deque

class Node:
    def __init__(self, val=None, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

#TC: O(n)
#TS : O(n)
def cloneGraph(node):
    if not node:
        return None

    # Initialize dict to mapper original node to cloned nodes
    node_mapping = {}

    # Inicialize the queue to BFS
    queue = deque([node])

    # Initial node cloned
    cloned_node = Node(node.val)
    node_mapping[node] = cloned_node

    while queue:
        current_node = queue.popleft()

        # visiting each node from actual node
        for neighbor in current_node.neighbors:
            # check if neighbor was visited
            if neighbor not in node_mapping:
                # Crie um nó clonado para o vizinho
                # Create a new cloned node
                cloned_neighbor = Node(neighbor.val)
                node_mapping[neighbor] = cloned_neighbor

                # Add the neighbor node to the queue to be processed in the future
                queue.append(neighbor)

            # Conecte o nó clonado atual aos nós clonados vizinhos
            # connect the current cloned node to the neighbor node cloned
            node_mapping[current_node].neighbors.append(node_mapping[neighbor])

    return node_mapping[node]
