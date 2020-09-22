from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # for item in nums:
        #     if nums.count(item)>=0:
        #         return item
        result=0
        for item in nums:
            result=result^item
        return result