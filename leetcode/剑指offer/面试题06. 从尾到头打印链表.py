from typing import List

class ListNode:
    def __init__(self, x,next=None):
        self.val = x
        self.next = next

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        result=[]
        while head:
            result.append(head.val)
            head=head.next
        result.reverse()
        return result

if  __name__=="__main__":
    head=None
    for item in range(5):
        print(item)
        head=ListNode(item,head)
    print(Solution().reversePrint(head))
