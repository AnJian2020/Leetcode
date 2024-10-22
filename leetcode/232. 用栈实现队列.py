# -*- coding: utf-8 -*-
# Generated by xuhao on 2021/3/26 14:00
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1=[]
        self.stack2=[]  # 辅助栈

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack1.append(x)


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        item=len(self.stack1)-1
        result=None
        while item>=0:
            if item!=0:
                self.stack2.append(self.stack1[item])
            else:
                result=self.stack1[item]
            self.stack1.pop(item)
            item-=1
        item2=len(self.stack2)-1
        while item2>=0:
            self.stack1.append(self.stack2[item2])
            self.stack2.pop(item2)
            item2-=1
        return result


    def peek(self) -> int:
        """
        Get the front element.
        """
        item = len(self.stack1) - 1
        result = None
        while item >= 0:
            if item==0:
                result=self.stack1[item]
            self.stack2.append(self.stack1[item])
            self.stack1.pop(item)
            item -= 1
        item2 = len(self.stack2) - 1
        while item2 >= 0:
            self.stack1.append(self.stack2[item2])
            self.stack2.pop(item2)
            item2 -= 1
        return result


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.stack1)==0



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()