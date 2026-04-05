# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:


        # tracerse to get all nodes
        nodes = []

        current_node = head
        while current_node is not None:
            nodes.append(current_node)
            current_node = current_node.next
        print(len(nodes))

        node_to_remove = nodes[-n]
        print("node to remove", node_to_remove.val)

        if node_to_remove == nodes[0]: # removing head
            if len(nodes) != 1:
                return nodes[1]
            else:
                return None

        prev_node = nodes[-n - 1]
        prev_node.next = node_to_remove.next

        return head


        