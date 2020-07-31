from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        #reversed(s)
        count=int(len(s)/2)
        length=len(s)
        for item in range(count):
            temp=s[item]
            s[item]=s[length-item-1]
            s[length-item-1]=temp

if __name__=="__main__":
    Solution().reverseString(['h','e','l','l','o','a'])