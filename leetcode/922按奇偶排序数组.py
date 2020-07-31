import itertools
from typing import List
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        a0=[]   #奇列表
        a1=[]   #偶列表
        for item in A:
            if item %2!=0:
                a0.append(item)
            else:
                a1.append(item)
        i=0
        result=[]
        while i<len(A):
            if i%2!=0:
                result.append(a0[0])
                a0.pop(0)
            elif i%2==0:
                result.append(a1[0])
                a1.pop(0)
            i+=1
        return result



if __name__=="__main__":
    A=[4,2,5,7]
    print(Solution().sortArrayByParityII(A))