# 翻转一棵二叉树。 
# 
#  示例： 
# 
#  输入： 
# 
#       4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9 
# 
#  输出： 
# 
#       4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1 
# 
#  备注: 
# 这个问题是受到 Max Howell 的 原问题 启发的 ： 
# 
#  谷歌：我们90％的工程师使用您编写的软件(Homebrew)，但是您却无法在面试时在白板上写出翻转二叉树这道题，这太糟糕了。 
#  Related Topics 树 
#  👍 636 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # 递归
        if root is None:
            return None
        # left=self.invertTree(root.right)
        # right=self.invertTree(root.left)
        # root.left,root.right=left,right
        # return root
        # 迭代
        queue=[root]
        while queue:
            tmp=queue.pop(0)
            tmp.left,tmp.right=tmp.right,tmp.left
            if tmp.left:
                queue.append(tmp.left)
            if tmp.right:
                queue.append(tmp.right)
        return root
# leetcode submit region end(Prohibit modification and deletion)
