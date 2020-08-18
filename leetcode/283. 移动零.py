from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        first=0
        last=1
        if len(nums)>1:
            for item in range(len(nums)-1):
                if nums[first]==0:
                    if nums[last]==0:
                        last+=1
                    elif nums[last]!=0:
                        nums[first]=nums[last]
                        nums[last]=0
                        first+=1
                        last+=1
                else:
                    last+=1
                    first+=1

if __name__=="__main__":
    nums=[1,0,1]
    Solution().moveZeroes(nums)
    print(nums)