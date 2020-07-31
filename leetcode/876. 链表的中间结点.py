#89342

class ListNode(object):
    def __init__(self,value,next=None):
        self.value=value
        self.next=next

class Solution:
    #快慢指针
    def middleNode(self, head: ListNode) -> ListNode:
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        return slow