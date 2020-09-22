from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        for item in range(k):
            tmp=nums.pop(-1)
            nums.insert(0,tmp)

if __name__=="__main__":
    nums=[1,2,3,4,5,6,7]
    Solution().rotate(nums,3)
    print(nums)