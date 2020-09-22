import collections
from typing import List



class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # numsset=set(nums)
        # for item in numsset:
        #     if nums.count(item)>len(nums)/2:
        #         return item
        # counts=collections.Counter(nums)
        # return max(counts.keys(),key=counts.get)
        nums.sort()
        return nums[int(len(nums)/2)]

if __name__=="__main__":
    nums=[2,2,1,1,1,2,2]
    print(Solution().majorityElement(nums))