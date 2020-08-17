from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        numsLength=len(nums)
        item1=0
        for item2 in range(numsLength):
            if nums[item2]!=val:
                nums[item1]=nums[item2]
                item1+=1
        return item1

if __name__=="__main__":
    print(Solution().removeElement([3,2,2,3],3))
