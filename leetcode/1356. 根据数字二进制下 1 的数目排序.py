import operator
from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort()
        numCount=[]
        for item in arr:
            oneCount=list(bin(item).replace("0b",""))
            numCount.append([item,oneCount.count("1")])
        result=sorted(numCount,key=lambda x:x[1])
        lastRe=[]
        for item in result:
            lastRe.append(item[0])
        return lastRe

if __name__=="__main__":
    arr = [0,1,1,2,3,4,5,6,7,8]
    print(Solution().sortByBits(arr))

