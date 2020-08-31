# -*- coding:utf-8 -*-

class TreeNode(object):
    def __init__(self, data, leftChild=None, rightChild=None):
        self.data = data
        self.leftChild = leftChild
        self.rightChild = rightChild


class Tree(object):
    def __init__(self, root=None):
        self.root = root

    def append(self, item):
        treeNode = TreeNode(item)
        if not self.root:
            self.root = treeNode
            return
        else:
            stack = []
            stack.append(self.root)
            while stack:
                currentTreeNode = stack.pop(0)
                if currentTreeNode.leftChild is None:
                    currentTreeNode.leftChild = treeNode
                    return
                elif currentTreeNode.rightChild is None:
                    currentTreeNode.rightChild = treeNode
                    return
                else:
                    stack.append(currentTreeNode.leftChild)
                    stack.append(currentTreeNode.rightChild)


class MiddleOrderTraversal(object):

    def middleOrderTraversalRecursion(self, treeNode):
        """
        二叉树中序遍历实现
        :return:
        """
        if treeNode is None:
            return
        self.middleOrderTraversalRecursion(treeNode.leftChild)
        print(treeNode.data.data)
        self.middleOrderTraversalRecursion(treeNode.rightChild)

    def middleOrderTraversalNotRescursion(self, treeNode):
        """
        中序遍历的非递归实现
        :param treeNode:
        :return:
        """
        stack = []
        result = []
        while treeNode or stack:
            if treeNode:
                stack.append(treeNode)
                treeNode = treeNode.leftChild
            else:
                currentNode = stack.pop()
                result.append(currentNode.data.data)
                treeNode = currentNode.rightChild
        print(result)


if __name__ == "__main__":
    tree = Tree()
    treeList = ['A', 'B', 'C', 'D', 'E']
    for item in treeList:
        tree.append(TreeNode(item))
    MiddleOrderTraversal().middleOrderTraversalRecursion(tree.root)
