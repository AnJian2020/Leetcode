from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i,j=0,len(nums)-1
        while i<j:
            s=nums[i]+nums[j]
            if s>target:
                j-=1
            elif s<target:
                i += 1
            else:
                return [nums[i],nums[j]]
        return []


if __name__=="__main__":
    nums=[2,7,11,15]
    target=9
    print(Solution().twoSum(nums,target))
