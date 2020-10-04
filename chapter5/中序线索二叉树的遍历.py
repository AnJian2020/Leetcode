"""
中序线索二叉树的遍历
"""
from typing import List


class ThreadNode(object):

    def __init__(self,data,lchild=None,rchild=None,ltag=0,rtag=0):
        self.data=data
        self.lchild=lchild
        self.rchild=rchild
        self.ltag=ltag
        self.rtag=rtag

class Solution(object):

    def findFirstNode(self,p:ThreadNode)->ThreadNode:
        """
        中序线索二叉树中中序序列的第一个节点
        :param p:
        :return:
        """
        while p.ltag==0:
            p=p.lchild
        return p

    def findNextNode(self,p:ThreadNode)->ThreadNode:
        """
        中序线索二叉树中节点p在中序序列下的后继
        :param p:
        :return:
        """
        if p.rtag==0:
            return self.findFirstNode(p.rchild)
        else:
            return p.rchild

    def Inorder(self,t:ThreadNode)->List:
        """
        中序遍历中序线索二叉树，返回含有结果的列表
        :param t:
        :return:
        """
        result=list()
        p=self.findFirstNode(t)
        while p is not None:
            result.append(p.data)
            p=self.findNextNode(p)
        return result

