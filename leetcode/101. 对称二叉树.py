class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# class Solution:
#     def isSymmetric(self, root: TreeNode) -> bool:
#         def visitTree(root:TreeNode):
#             stack=[]
#             result=[]
#             while root or stack:
#                 if root:
#                     stack.append(root)
#                     root=root.left
#                 else:
#                     currentNode=stack.pop()
#                     result.append(currentNode.val)
#                     root = currentNode.right
#             return result
#
#         result=visitTree(root)
#         p,t=0,len(result)-1
#         while p!=t:
#             if result[p]!=result[t]:
#                 return False
#             p+=1
#             t-=1
#         return True
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        def compare(leftTree:TreeNode,rightTree:TreeNode)->bool:
            if not leftTree and not rightTree:
                return True
            if not leftTree or not rightTree:
                return False
            if leftTree.val!=rightTree.val:
                return False
            return compare(leftTree.left,rightTree.right) and compare(leftTree.right,rightTree.left)
        return compare(root.left,root.right)