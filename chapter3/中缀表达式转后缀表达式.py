# -*- coding:utf-8 -*-

from chapter3.Stack.Stack import Stack
class Solution(object):

    def __init__(self):
        self.__stack=Stack(50)
        self.__sign=['(',')','-','+','*','/']
        self.__equationResult=[]

    def conversion(self,equation):
        for item in equation:
            if item not in self.__sign:
                self.__equationResult.append(item)
            else:
                if self.__stack.isEmpty():
                    self.__stack.push(item)
                elif item in '*/(':
                    self.__stack.push(item)
                elif item==")":
                    tmp=self.__stack.pop()
                    while tmp!='(':
                        self.__equationResult.append(tmp)
                        tmp=self.__stack.pop()
                elif item in '+-' and self.__stack.getTop() in '*/':
                    if self.__stack.count('(')==0:
                        while not self.__stack.isEmpty():
                            tmp=self.__stack.pop()
                            self.__equationResult.append(tmp)
                    else:
                        tmp=self.__stack.pop()
                        while tmp!='(':
                            self.__equationResult.append(tmp)

                            tmp = self.__stack.pop()
                        self.__stack.push('(')
                    self.__stack.push(item)
                else:
                    self.__stack.push(item)
        while not self.__stack.isEmpty():
            tmp=self.__stack.pop()
            self.__equationResult.append(tmp)

        return ''.join(self.__equationResult)



if __name__=="__main__":
    print(Solution().conversion(['a','+','b','-','a','*','(','(','c','+','d',')','/','e','-','f',')','+','g']))




