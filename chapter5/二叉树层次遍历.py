# -*- coding:utf-8 -*-

class TreeNode(object):
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right

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

class LevelOrder():

    def levelOrder(self,treeNode):
        queue=[]
        result=[]
        queue.append(treeNode)
        while queue:
            currentNode=queue.pop(0)
            result.append(currentNode.data.data)
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
        return result

if __name__=="__main__":
    treeList=['A','B','C','D','E','F','G']
    tree=Tree()
    for item in treeList:
        tree.add(TreeNode(item))
    print(LevelOrder().levelOrder(tree.root))
