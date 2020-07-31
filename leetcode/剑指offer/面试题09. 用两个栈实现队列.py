# -*- coding:utf-8 -*-

class CQueue(object):

    def __init__(self):
        self.stack_in=[]
        self.stack_out=[]

    def appendTail(self, value: int) -> None:
        self.stack_in.append(value)

    def deleteHead(self) -> int:
        if not self.stack_out:
            if not self.stack_in:
                return -1
            else:
                while self.stack_in:
                    self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop()


