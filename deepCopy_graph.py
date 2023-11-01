# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional

class Solution:
    visited = {}
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        root = Node(node.val)
        myQ = [(node, root)]
        
        while myQ:
            item, itmcopy = myQ.pop(0)
            if item not in self.visited:
                self.visited[item] = itmcopy
            for neigh in item.neighbors:
                if neigh not in self.visited:
                    new_neigh = Node(neigh.val)
                    itmcopy.neighbors.append(new_neigh)
                    myQ.append((neigh, new_neigh))
                else:
                    itmcopy.neighbors.append(self.visited[neigh])

        return root

# Create the graph based on the provided adjacency list
# Graph: [[2,4],[1,3],[2,4],[1,3]]
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]

# Clone the graph using the Solution class
solution = Solution()
cloned_node = solution.cloneGraph(node1)

# Check if the cloned graph is correct by printing the neighbors of the cloned nodes
for node in [node1, node2, node3, node4]:
    print(f"Original Node {node.val}: {[neighbor.val for neighbor in node.neighbors]}")
    cloned = solution.visited[node]
    print(f"Cloned Node {cloned.val}: {[neighbor.val for neighbor in cloned.neighbors]}")
