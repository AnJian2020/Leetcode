import collections
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Tree(object):
    def __init__(self,root=None):
        self.root=root

    def add(self,item):
        treeNode=TreeNode(item)
        if not self.root:
            self.root=treeNode
            return
        else:
            stack=[]
            stack.append(self.root)
            while stack:
                currentNode=stack.pop(0)
                if currentNode.left is None:
                    currentNode.left=treeNode
                    return
                elif currentNode.right is None:
                    currentNode.right=treeNode
                    return
                else:
                    stack.append(currentNode.left)
                    stack.append(currentNode.right)
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        def levelOrder(root: TreeNode) -> List[List[int]]:
            if not root:
                return []
            res = []
            d = collections.deque()
            d.append(root)
            while d:
                n = len(d)
                tmp = []
                for i in range(n):
                    node = d.popleft()
                    tmp.append(node.val)
                    if node.left:
                        d.append(node.left)
                    if node.right:
                        d.append(node.right)
                res.append(tmp)
            return res

        return levelOrder(root)[::-1]

if __name__=="__main__":
    treeList=[[3,9,20,None,None,15,7]]
    t=reversed(treeList)
    print(t)
    tree=Tree()
    for item in treeList:
        tree.add(TreeNode(item))
    print(Solution().levelOrderBottom(tree.root))