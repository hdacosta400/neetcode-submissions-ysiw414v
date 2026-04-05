# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        '''

        traverse linked list to get pointer to each node 

        use two pointers to interleave beginning / end nodes

        '''

        # traverse liknked linked 
        nodes = []
        nodes.append(head)
        current_node = head.next
        while current_node is not None:
            nodes.append(current_node)
            # update
            current_node = current_node.next
        print("number of nodes", len(nodes))


        # interleave
        left , right = 0, len(nodes) - 1

        while left < right:
            nodes[left].next = nodes[right]
            left += 1
            if left == right:
                break
            nodes[right].next = nodes[left]
            right -= 1
        nodes[left].next = None
        