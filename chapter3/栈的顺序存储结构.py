# coding:utf-8

#author:xuhao

class StackSort(object):

    # 初始化栈
    def __init__(self,MAXSIZE):
        self.item=[ item for item in range(MAXSIZE) ]
        self.top=-1
        self.MAXSIZE=MAXSIZE

    # 判断栈是否为空
    def stackEmpty(self)->bool:
        if self.top==-1:
            return True
        else:
            return False

    # 进栈
    def push(self,x)->bool:
        if self.top==self.MAXSIZE-1:
            return False
        self.top+=1
        self.item[self.top]=x
        return True

    # 出栈
    def pop(self)->bool:
        if self.top==-1:
            return False
        self.item.pop(self.top)
        self.top-=1
        return True

    def getTop(self):
        if self.top==-1:
            return -1
        return self.item[self.top]

if __name__=="__main__":
    stack=StackSort(5)
    stack.push('a')
    print(stack.getTop())
