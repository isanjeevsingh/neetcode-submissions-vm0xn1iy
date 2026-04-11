# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        import math as mt
        Q = [(root, -mt.inf, mt.inf)]

        while Q:
            node, left, right = Q.pop()

            if not left < node.val < right:
                return False
            
            if node.left:
                Q.append((node.left, left, node.val))
            if node.right:
                Q.append((node.right, node.val, right))
        
        return True