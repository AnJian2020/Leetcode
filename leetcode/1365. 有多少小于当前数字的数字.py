from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result=[]
        for item in nums:
            count=0
            for minItem in nums:
                if minItem<item:
                    count+=1
            result.append(count)
        return result

if __name__=="__main__":
    nums= [8,8,8]
    print(Solution().smallerNumbersThanCurrent(nums))
