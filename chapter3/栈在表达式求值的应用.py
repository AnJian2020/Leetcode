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
        if self.__top==-1:
            return False
        self.__item.pop(self.__top)
        self.__top-=1
        return True

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

class ExpressionEvaluation(object):
    def __init__(self):
        self.__stack=Stack(20)
        self.__sign=['-','+','/','*']

    def getExpressionEvaluation(self,equation):
        equation=list(equation)
        for item in equation:
            if item not in self.__sign:
                self.__stack.push(item)
            elif item in self.__sign:
                num1=self.__stack.getTop()
                self.__stack.pop()
                num2=self.__stack.getTop()
                self.__stack.pop()
                if item=="+":
                    self.__stack.push(num1+num2)
                elif item=="-":
                    self.__stack.push(num2 - num1)
                elif item=="/":
                    self.__stack.push(num2 / num1)
                elif item=="*":
                    self.__stack.push(num1*num2)
        return self.__stack.getTop()

if __name__=="__main__":
     print(ExpressionEvaluation().getExpressionEvaluation([50,3,5,4,'-','*','+',7,9,'/','-']))
