class TreeNode:
    def __init__(self, x,left=None,right=None):
        self.val = x
        self.left = left
        self.right = right

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
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            leftDepth=self.maxDepth(root.left)
            rightDepth=self.maxDepth(root.right)
        return max(leftDepth,rightDepth)+1


if __name__=="__main__":
    treeNodeList=[3,9,20,None,None,15,7]
    tree = Tree()
    for item in treeNodeList:
        tree.add(TreeNode(item))
    print(Solution().maxDepth(tree))
