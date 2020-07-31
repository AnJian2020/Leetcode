# -*- coding:utf-8 -*-

#author:@xuhao

from chapter2.SingleNode import SingleNode

"""
单链表
"""
class SingleList(object):

    def __init__(self,node=None):
        self.head=node

    def length(self)->int:
        count=0
        while self.head!=None:
            count+=1
            self.head=self.head.next
        return count

    def ListHeadInsert(self,value:int):
        newNode=SingleNode(value)
        newNode.next=self.head
        self.head=None

    def ListTailInsert(self,value:int):
        newNode=SingleNode(value)
        if self.isEmpty():
            self.head=newNode
        else:
            while self.head.next:
                self.head=self.head.next
            self.head.next=newNode

    def isEmpty(self):
        if self.head==None:
            return True
        else:
            return False

    def getElem(self,i:int):
        j=1
        while self.head!=None and j<i:
            self.head=self.head.next
            j+=1
        return self.head

    def locateElem(self,i:int):
        while self.head and self.head.data!=i:
            self.head=self.head.next
        return self.head

    def insertNode(self,value,i):
        prior=SingleList(self.head).getElem(i-1)
        newNode=SingleNode(value)
        newNode.next=prior.next
        prior.next=newNode

    def deleteNode(self,i:int)->bool:
        if i<1 or i>SingleList(self.head).length():
            return False
        tem=SingleList(self.head).getElem(i-1)
        tem.next=tem.next.next
        return True

if __name__=="__main__":
    head=None
    for count in range(1,6):
        head=SingleNode(count,head)
    SingleList(head).deleteNode(3)
    while head!=None:
        print(head.data)
        head=head.next

