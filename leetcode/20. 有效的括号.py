# -*- coding:utf-8 -*-

# author: xuhao

# @Time: 2020/4/17

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2==1:
            return False
        stackItem=[]
        stack_l={')':'(',']':'[','}':'{'}
        strlist=list(s)
        for item in strlist:
            if item in stack_l.values():
                stackItem.append(item)
            elif item in stack_l.keys():
                if len(stackItem)==0:
                    return False
                if stack_l[item]==stackItem[-1]:
                    stackItem.pop()
                else:
                    return False
        if len(stackItem)==0:
            return True
        else:
            return False

if __name__=="__main__":
    print(Solution().isValid(')}'))
