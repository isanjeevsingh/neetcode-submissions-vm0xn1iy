# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        L = []
        if not root:
            return L
        
        Q = [root]
        level = 1
        while Q:
            l = []
            next_level = 0
            for _ in range(level):
                q = Q.pop(0)
                l.append(q.val)
                if q.left: 
                    Q.append(q.left)
                    next_level += 1
                if q.right: 
                    Q.append(q.right)
                    next_level += 1
            L.append(l)
            level = next_level
        return L