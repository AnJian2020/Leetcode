class ListNode(object):
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

class Solution(object):
    def hasCycle(self,head:ListNode)->bool:
        if head==None or head.next==None:
            return False
        slow=head
        fast=head.next
        while slow!=fast:
            if fast==None or fast.next==None:
                return False
            slow=slow.next
            fast=fast.next.next
        return True

