# -*- coding:utf-8 -*-

#author:xuhao

from chapter2.SingleNode import SingleNode as Node

class StackLink():

    def __init__(self):
        self.head=None

    def stackEmpty(self)->bool:
        return self.head==None

    def push(self,data):
        self.head=Node(data,self.head)

    def pop(self)->bool:
        if self.head==None:
            return False
        self.head=self.head.next

    def getTop(self):
        if self.head==None:
            return -1
        return self.head.data

if __name__=="__main__":
    stack=StackLink()
    stack.push('a')
    stack.push('b')
    stack.push('c')
    stack.pop()
    print(stack.getTop())



