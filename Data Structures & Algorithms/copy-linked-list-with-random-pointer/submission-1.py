"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if head is None:
            return None

        # populate original -> copy node map
        node_map = {}
        current_node = head
        while current_node is not None:
            if current_node not in node_map:
                node_map[current_node] = Node(current_node.val)
            current_node = current_node.next


        for node in node_map:
            original_node_next = node.next
            original_node_random = node.random

            if original_node_next is not None:
                node_map[node].next = node_map[original_node_next]

            if original_node_random is not None:
                node_map[node].random = node_map[original_node_random]
        return node_map[head]        


        