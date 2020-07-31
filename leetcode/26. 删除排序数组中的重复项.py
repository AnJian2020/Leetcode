from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count=0
        for item in range(1,len(nums)):
            if nums[item]!=nums[count]:
                count += 1
                nums[count]=nums[item]
        return count+1

if __name__=="__main__":
    nums=[1,1,2]
    print(Solution().removeDuplicates(nums))
