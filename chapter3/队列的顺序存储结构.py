# -*- coding:utf-8 -*-

# author: xuhao

class QueueList(object):
    def __init__(self,MaxSize):
        self.item=list()
        for count in range(MaxSize):
            self.item.append(None)
        self.front=self.rear=0
        self.MaxSize=MaxSize

    def isEmpty(self)->bool:
        if self.front==self.rear:
            return True
        else:
            return False

    def enQueue(self,x)->bool:
        if self.front==(self.rear+1)%self.MaxSize:
            return False
        self.item[self.rear]=x
        self.rear=(self.rear+1)%self.MaxSize
        return True

    def deQueue(self)->bool:
        if self.rear==self.front:
            return False
        self.front=(self.front+1)%self.MaxSize
        return True

    def getHead(self):
        if self.front==self.rear:
            return None
        return self.item[self.front]

if __name__=="__main__":
    queue=QueueList(5)
    for item in range(5):
        queue.enQueue(item)
    queue.deQueue()
    print(queue.getHead())



