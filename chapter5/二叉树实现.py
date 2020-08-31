# -*- coding:utf-8 -*-

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
        if not self.root:
            self.root=treeNode
            return
        else:
            stack=list()
            stack.append(self.root)
            while stack:
                currentTreeNode=stack.pop(0)
                if currentTreeNode.leftChild is None:
                    currentTreeNode.leftChild=treeNode
                    return
                elif currentTreeNode.rightChild is None:
                    currentTreeNode.rightChild=treeNode
                    return
                else:
                    stack.append(currentTreeNode.leftChild)
                    stack.append(currentTreeNode.rightChild)


if __name__=="__main__":
    treeList=[1,2,3,4,5,6,7,8]
    tree=Tree()
    for item in treeList:
        tree.append(item)
        print()
