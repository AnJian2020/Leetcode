# -*- coding:utf-8 -*-

#author:@xuhao

from chapter2.DoubleNode import DoubleNode as Node

class DoubleList(object):

    def __init__(self,node=None):
        self.head=node

    def length(self):
        count=0
        while self.head!=None:
            count+=1
            self.head=self.head.next
        return count

    def isEmpty(self):
        if self.head is None:
            return False
        else:
            return True

    def getElem(self,i):
        count=0
        while self.head!=None and count<i:
            self.head=self.head.next
            count+=1
        return self.head

    def insertLink(self,value,i):
        p=DoubleList(self.head).getElem(i-1)
        newNode=Node(value)
        newNode.next=p.next
        p.next.prior=newNode
        newNode.prior=p
        p.next=newNode

    def deleteLink(self,i):
        p=DoubleList(self.head).getElem(i-1)
        q=p.next
        p.next=q.next
        q.next.prior=p

    def searchNode(self,value):
        while self.head:
            if self.head.data==value:
                return self.head
            else:
                self.head=self.head.next

if __name__=="__main__":
    head=Node(1)
    prior=head
    for count in range(2,6):
        prior.next=Node(count,prior=prior)
        prior=prior.next
    while head!=None:
        print(head.data)
        head=head.next
    print("------")
    while prior!=None:
        print(prior.data)
        prior=prior.prior

