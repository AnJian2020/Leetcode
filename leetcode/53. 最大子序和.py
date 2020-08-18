from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for item in range(1,len(nums)):
            nums[item]=nums[item]+max(nums[item-1],0)
        return max(nums)


if __name__=="__main__":
    print(Solution().maxSubArray([-2,1]))