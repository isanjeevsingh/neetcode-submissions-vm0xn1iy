# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import math as mt

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        Q = [(root, -mt.inf)]
        res = 0
        while Q:
            q = Q.pop(0)
            if q[0].val >= q[1]:
                res += 1
            
            if q[0].left:
                Q.append((q[0].left, max(q[0].val, q[1])))
            if q[0].right:
                Q.append((q[0].right, max(q[0].val, q[1])))
        return res