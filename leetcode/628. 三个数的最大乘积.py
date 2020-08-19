from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums=sorted(nums)
        result=[]
        result.append(nums[-1]*nums[-2]*nums[-3])
        result.append(nums[0]*nums[1]*nums[-1])
        return max(result)


if __name__=="__main__":
    print(Solution().maximumProduct([-4,-3,-2,-1,60]))

