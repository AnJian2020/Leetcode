# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if (not p and q) or (p and not q) or (p.val!=q.val):
            return False
        else:
            return self.isSameTree(p.right,q.right) and self.isSameTree(p.left,q.left)