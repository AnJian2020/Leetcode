class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        elif root.left is None and root.right is None:
            return 1
        else:
            depth=10**9
            if root.left:
                depth=min(self.minDepth(root.left),depth)
            if root.right:
                depth=min(self.minDepth(root.right),depth)
        return depth+1