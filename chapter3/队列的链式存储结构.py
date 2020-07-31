# -*- coding:utf-8 -*-

# author:xuhao

class Node(object):

    def __init__(self,data,next=None):
        self.data=data
        self.next=next

class QueueLink(object):

    def __init__(self):
        self.front=self.rear=Node(None)
        self.front.next=None

    def isEmpty(self):
        return self.front==self.rear

    def enQueue(self,x):
        s=Node(x)
        if self.front.data== None:
            self.front=s
            self.rear=s
        else:
            self.rear.next=s
            self.rear=s

    def deQueue(self):
        if self.rear==self.front:
            return False
        self.front=self.front.next
        return True

    def getHead(self):
        if self.front==self.rear:
            return None
        else:
            return self.front.data

if __name__=="__main__":
    queue=QueueLink()
    for item in range(5):
        queue.enQueue(item)
    queue.deQueue()
    print(queue.getHead())


