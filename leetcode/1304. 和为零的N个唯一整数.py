from typing import List

class Solution:
    def sumZero(self, n: int) -> List[int]:
        result=[]
        sum=0
        if n==1:
            return [0]
        for item in range(n-1):
            result.append(item)
            sum+=item
        result.append(-sum)
        return result

if __name__=="__main__":
    print(Solution().sumZero(1000))

