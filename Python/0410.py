# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def checkSubTree(self, t1: TreeNode, t2: TreeNode) -> bool:
        if not t1 and not t2:
            return True

        if not t1 or not t2:
            return False

        if t1 and t2:
            return (t1.val == t2.val and self.checkSubTree(t1.left,t2.left) and self.checkSubTree(t1.right,t2.right)) or self.checkSubTree(t1.right,t2) or self.checkSubTree(t1.left,t2)