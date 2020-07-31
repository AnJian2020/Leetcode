from typing import List


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result=[]
        item=0
        while item<len(nums):
            for i in range(nums[item]):
                result.append(nums[item+1])
            item+=2
        return  result

if __name__=="__main__":
    nums = [1, 2, 3, 4,5,6,7,8]
    print(Solution().decompressRLElist(nums))