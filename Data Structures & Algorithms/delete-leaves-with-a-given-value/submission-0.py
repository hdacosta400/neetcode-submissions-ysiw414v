# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        

        if self.isLeafNode(root):
            if root.val == target:
                return None
            return root
        
        # not a leaf node
        if root.left:
            root.left = self.removeLeafNodes(root.left, target)
        if root.right:
            root.right = self.removeLeafNodes(root.right, target)
        
        if self.isLeafNode(root):
            if root.val == target:
                return None
            return root
        

        return root
    
    def isLeafNode(self, node: TreeNode):
        return node.left is None and node.right is None
