class ListNode(object):
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

class Solution(object):
    def isPalindrome(self, head: ListNode) -> bool:
        nums=[]
        while head!=None:
            nums.append(head.val)
            head=head.next

        return nums==nums[::-1]

if __name__=="__main__":
    head=None
    for item in range(1,3):
        head=ListNode(0,head)
    print(Solution().isPalindrome(head))

