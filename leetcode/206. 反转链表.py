# -*- coding:utf-8 -*-
#author:xuhao

class ListNode(object):
    def __init__(self,value,next=None):
        self.value=value
        self.next=next

class Solution(object):
    def reverseList(self,head:ListNode)->ListNode:
        if head==None:
            return None
        prev=None
        while head!=None:
            head.next=prev
            prev=head
            head=head.next
        return prev


