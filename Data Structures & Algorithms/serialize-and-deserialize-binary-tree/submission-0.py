# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return "null"
        
        result_str = ""
        result_str += str(root.val) + ","
        result_str += self.serialize(root.left) + ","
        result_str += self.serialize(root.right)
    
        return result_str
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        tree_list = deque(data.split(","))

        if tree_list == []:
            return []
        
        def __helper():
            current_val = tree_list.popleft()
            if current_val == "null":
                return None
            node = TreeNode(current_val)
            node.left = __helper()
            node.right = __helper()
            return node
        return __helper()


    


        
