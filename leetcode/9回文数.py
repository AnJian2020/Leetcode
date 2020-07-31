"""
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        num1=list(str(x))
        num2=[]
        if len(num1)==1:
            return True
        else:
            i=len(num1)-1
            while i>=0:
                if num1[0]!="-" and num1[-1]!="0":
                    num2.append(num1[i])
                i-=1
            if num1==num2:
                return True
            else:
                return False


if __name__=="__main__":
    print(Solution().isPalindrome(-1001))
