from typing import List

class Solution:
    def deleteAgain(self,num:List):
        if len(num)==0:
            return False
        i=0
        j=1
        while j<len(num):
            if num[i]!=num[j]:
                i+=1
                num[i]=num[j]
            j+=1
        print(num[:i+1])
        return True
if __name__=="__main__":
    num=[1, 2, 2, 3, 3, 4, 4, 6, 7]
    Solution().deleteAgain(num)