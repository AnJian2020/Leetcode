class ListNode:
    def __init__(self, x,next=None):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        cur=head
        while head != None and head.next != None:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
        return cur


if __name__=="__main__":
    head=None
    head=ListNode(1,head)
    head=ListNode(1,head)
    head=ListNode(2,head)
    head=Solution().deleteDuplicates(head)
    while head!=None:
        print(head.val)
        head=head.next