from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        numStr=[]
        for item in nums:
            numStr.append(list(str(item)))
        result=0

        for item in numStr:

            if len(item)%2==0:
                result+=1
        return result

if __name__=="__main__":
    nums= [555,901,482,1771]
    print(Solution().findNumbers(nums))