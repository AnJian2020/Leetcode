# -*- coding:utf-8 -*-
#author:xuhao

from chapter2.SingleNode import SingleNode as Node

class Soulation(object):
    def deleteValue(self,head,x):
        if head==None:
            return False
        elif head.data==x and head.next==None:
            head=None
            return True
        q=head.next
        while q!=None:
            if q.data==x:
                q = q.next
                head.next=q
            else:
                head=q
                q=q.next
        return True


if __name__=="__main__":
    head=None
    for item in range(1,10):
        head=Node(item,head)
    if Soulation().deleteValue(head,9):
        while head!=None:
            print(head.data)
            head=head.next








