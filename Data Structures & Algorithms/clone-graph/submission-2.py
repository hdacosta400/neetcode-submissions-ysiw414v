"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        adj_dict = {}

        queue = [node]
        num_nodes = 1
        while queue:
            curr_node = queue.pop()

            if curr_node.val not in adj_dict:
                adj_dict[curr_node.val] = []
            
                adj_dict[curr_node.val].extend([n.val for n in curr_node.neighbors])

                for n in curr_node.neighbors:
                    if n.val > num_nodes:
                        num_nodes = n.val
                    queue.append(n)

        nodes = [Node(i) for i in range(1, num_nodes + 1)]
        for n in nodes:
            recorded_neighbors = adj_dict[n.val]
            copied_neighbors = [nodes[i - 1] for i in recorded_neighbors]
            n.neighbors = copied_neighbors
        return nodes[0]


