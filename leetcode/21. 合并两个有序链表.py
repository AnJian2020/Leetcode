#89342

class ListNode(object):
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1==None:
            return l2
        if l2==None:
            return l1

        while l1 and l2:
            if l1.val<=l2.val:
                l1.next=Solution().mergeTwoLists(l1.next,l2)
                return l1
            else:
                l2.next=Solution().mergeTwoLists(l1,l2.next)
                return l2


