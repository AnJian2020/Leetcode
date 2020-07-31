from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        num1=[] #正
        num2=[] #负
        result=[]
        for item in sorted(nums):
            if item>=0:
                num1.append(item)
            else:
                num2.append(item)
        if len(num1)==1:
            result.append(num1[-1]*num2[0]*num2[1])
        elif len(num1)==0:
            result.append(num2[-1]*num2[-2]*num2[-3])
        elif len(num1)==2:
            result.append(num1[-1]*num1[-2]*num2[-1])
        elif len(num1)>2:
            result.append(num1[-1]*num1[-2]*num1[-3])
        return max(result)


if __name__=="__main__":
    print(Solution().maximumProduct([-4,-3,-2,-1,60]))

