# -*- coding:utf-8 -*-

# author:@xuhao

from chapter2.SingleNode import SingleNode

class Soulation(object):

    def deleteValue(self,head,value):
        if head==None or head.next==None:
            return False
        if head.next.data==value:
            head.next=head.next.next
            Soulation().deleteValue(head,value)
        else:
            Soulation().deleteValue(head.next,value)
        return True

if __name__=="__main__":
    head=None
    for count in range(1,7):
        head=SingleNode(count,head)
    if Soulation().deleteValue(head,2):
        while head!=None:
            print(head.data)
            head=head.next
    else:
        print("error")
