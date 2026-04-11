# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        Q = [root]
        level = 1
        right_nodes = []
        while Q:
            next_level = 0
            for i in range(level):
                q = Q.pop(0)
                if i == level-1:
                    right_nodes.append(q.val)
                if q.left: 
                    Q.append(q.left)
                    next_level += 1
                if q.right: 
                    Q.append(q.right)
                    next_level += 1
            level = next_level
        return right_nodes
