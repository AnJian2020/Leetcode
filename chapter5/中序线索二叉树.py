# -*- coding:utf-8 -*-

class ThreadNode(object):
    def __init__(self,data,lchild=None,rchild=None,ltag=0,rtag=0):
        self.data=data
        self.lchild=lchild
        self.rchild=rchild
        self.ltag=ltag
        self.rtag=rtag

class MiddleOrderClueBinaryTree(object):
    # 中序线索二叉树的构建
    def inThread(self,p,pre):
        if p:
            self.inThread(p.lchild,pre)
            if p.lchild is None:
                p.lchild=pre
                p.ltag=1
            if pre is not None and pre.lchild is None:
                pre.lchild=p
                pre.rtag=1
            pre=p
            self.inThread(p.rchild,pre)

    def createInThread(self,t):
        pre=ThreadNode(data=None)
        if t is not None:
            self.inThread(t,pre)
            pre.rchild=None
            pre.rtag=1