from typing import List

class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort()
        i=0
        result=[]
        while i<len(A)-2:
            if A[i]+A[i+1]>A[i+2] and A[i+2]-A[i+1]<A[i]:
                result.append(A[i]+A[i+1]+A[i+2])
            i+=1
        return max(result)


if __name__=="__main__":
    a=[3,2,3,4]
    print(Solution().largestPerimeter(a))