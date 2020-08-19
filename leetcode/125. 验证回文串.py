class Solution:
    def isPalindrome(self, s: str) -> bool:
        strList1=[item.lower() for item in s if item.isalnum()]
        strList2=list(reversed(strList1))
        # i=0
        # while i<len(strList)/2:
        #     if strList[i]!=strList[len(strList)-1-i]:
        #         return False
        #     i+=1
        if strList1==strList2:
            return True
        return False

if __name__=="__main__":
    print(Solution().isPalindrome("race a car"))