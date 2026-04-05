# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        # traverse both lists to get nums, then add
        print("l1 num", self.get_number_from_list(l1))
        print("l2 num", self.get_number_from_list(l2))

        added_sum = self.get_number_from_list(l1) + self.get_number_from_list(l2)
        print("added ", added_sum)
        return self.get_list_from_number(added_sum)

    
    def get_number_from_list(self, linked_list):

        number = 0

        current_node = linked_list
        multiplier = 1

        while current_node is not None:

            number += current_node.val * multiplier
            multiplier *= 10
            current_node = current_node.next
        return number
    
    def get_list_from_number(self, number):
        number_str = str(number)

        head = None
        current_node = None
        for i in range(len(number_str) - 1, -1, -1):
            print("current num:", number_str[i])

            if current_node is None:
                current_node = ListNode(int(number_str[i]), None)

            next_node = None
            if i > 0:
                next_node = ListNode(int(number_str[i - 1]), None)

            current_node.next = next_node


            if head is None:
                head = current_node

            current_node = next_node
        
        print("what is head", head.val)
        return head
            



        