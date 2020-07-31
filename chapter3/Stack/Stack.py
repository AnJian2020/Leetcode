# -*- coding:utf-8 -*-

class Stack(object):

    #初始化栈
    def __init__(self,MaxSize):
        self.__item=[]
        for i in range(MaxSize):
            self.__item.append(None)
        self.__MaxSize=MaxSize
        self.__top=-1

    #出栈
    def pop(self):
        tmp=self.__item[self.__top]
        self.__item.pop(self.__top)
        self.__top-=1
        return tmp

    #入栈
    def push(self,val):
        if self.__top==self.__MaxSize:
            return False
        self.__top+=1
        self.__item[self.__top]=val
        return True

    #判断栈是否为空
    def isEmpty(self):
        return self.__top==-1

    #获取栈顶元素
    def getTop(self):
        return self.__item[self.__top]

    def count(self,x):
        return self.__item.count(x)
