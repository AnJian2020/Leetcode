# -*-coding:utf-8 -*-

class BiTree(object):
    def __init__(self, data, leftChild=None, rightChild=None):
        self.data = data
        self.leftChild = leftChild
        self.rightChild = rightChild


class Tree(object):
    def __init__(self, root=None):
        self.root = root

    def append(self, item):
        tree = BiTree(item)
        if not self.root:
            self.root = tree
            return
        else:
            stack = []
            stack.append(self.root)
            while stack:
                currentTreeNode = stack.pop(0)
                if currentTreeNode.leftChild is None:
                    currentTreeNode.leftChild = tree
                    return
                elif currentTreeNode.rightChild is None:
                    currentTreeNode.rightChild = tree
                    return
                else:
                    stack.append(currentTreeNode.leftChild)
                    stack.append(currentTreeNode.rightChild)


class MiddleOrderTraversal(object):

    def middleOrderTraversalRecursion(self, treeNode):
        """
        先序遍历的递归实现
        :param treeNode:
        :return:
        """
        if treeNode is None:
            return
        print(treeNode.data.data)
        self.middleOrderTraversalRecursion(treeNode.leftChild)
        self.middleOrderTraversalRecursion(treeNode.rightChild)

    def middleOrderTraversalNotRecursion(self, treeNode):
        """
        先序遍历的非递归实现
        :param treeNode:
        :return:
        """
        stack = []
        result = []
        while treeNode or stack:
            if treeNode:
                result.append(treeNode.data.data)
                stack.append(treeNode)
                treeNode = treeNode.leftChild
            else:
                currentNode = stack.pop()
                treeNode = currentNode.rightChild
        print(result)


if __name__ == '__main__':
    treeList = ['A', 'B', 'C', 'D', 'E']
    tree = Tree()
    for item in treeList:
        tree.append(BiTree(item))
    print("先序遍历的递归实现：")
    MiddleOrderTraversal().middleOrderTraversalRecursion(tree.root)
    print("先序遍历的非递归实现：")
    MiddleOrderTraversal().middleOrderTraversalNotRecursion(tree.root)
