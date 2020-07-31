from typing import List

class Solution:
    def resetList(self,numList:List,m:int,n:int)->List:
        numList.reverse()
        numList=sorted(numList[0:n+1])+sorted(numList[n+1:len(numList)])
        return numList

if __name__=="__main__":
    num=[1,2,3,4,5,6,7,8,9]
    print(Solution().resetList(num,3,5))
