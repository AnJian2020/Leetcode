# -*-coding:utf-8 -*-

class TreeNode(object):

    def __init__(self,data,leftChild=None,rightChild=None):
        self.data=data
        self.leftChild=leftChild
        self.rightChild=rightChild

class Tree(object):

    def __init__(self,root=None):
        self.root=root

    def append(self,item):
        treeNode=TreeNode(item)
        if self.root is None:
            self.root=treeNode
            return
        else:
            stack=[]
            stack.append(self.root)
            while stack:
                currentTreeNode=stack.pop(0)
                if currentTreeNode.leftChild is None:
                    currentTreeNode.leftChild = treeNode
                    return
                elif currentTreeNode.rightChild is None:
                    currentTreeNode.rightChild=treeNode
                    return
                else:
                    stack.append(currentTreeNode.leftChild)
                    stack.append(currentTreeNode.rightChild)

class PostorderTraversal(object):

    def postorderTraversalRecursion(self,treeNode):
        """
        后序遍历的递归实现
        :param treeNode:
        :return:
        """
        if treeNode is None:
            return
        self.postorderTraversalRecursion(treeNode.leftChild)
        self.postorderTraversalRecursion(treeNode.rightChild)
        print(treeNode.data.data)

    def postorderTraversalNotRecursion(self,treeNode):
        """
        后序遍历的非递归实现
        :param treeNode:
        :return:
        """
        stack=[]
        result=[]
        r=None

        while treeNode or stack:
            if treeNode:
                stack.append(treeNode)
                treeNode=treeNode.leftChild
            else:
                currentNode=stack[-1]
                if currentNode.rightChild and r!=currentNode.rightChild:
                    treeNode=currentNode.rightChild
                    stack.append(treeNode)
                    treeNode=treeNode.leftChild
                else:
                    currentNode=stack.pop()
                    result.append(currentNode.data.data)
                    r=currentNode
                    treeNode=None
        print(result)

if __name__=="__main__":
    treeNodeList=['A','B','C','D','E']
    tree=Tree()
    for item in treeNodeList:
        tree.append(TreeNode(item))
    PostorderTraversal().postorderTraversalRecursion(tree.root)
    PostorderTraversal().postorderTraversalNotRecursion(tree.root)