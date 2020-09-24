from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums)<=2:
            return []
        nums.sort()
        result=[]
        # for item1 in range(len(nums)-2):
        #     for item2 in range(item1+1,len(nums)-1):
        #         for item3 in range(item2+1,len(nums)):
        #             if nums[item1]+nums[item2]+nums[item3]==0 and [nums[item1],nums[item2],nums[item3]] not in result :
        #                 result.append([nums[item1],nums[item2],nums[item3]])
        for item1 in range(len(nums)-2):
            for item2 in range(item1+1,len(nums)-1):
                tmp=-(nums[item1]+nums[item2])
                if tmp in nums[(item2+1):len(nums)] and [nums[item1],nums[item2],tmp] not in result:
                    result.append([nums[item1],nums[item2],tmp])
        return result

if __name__=="__main__":
    nums= [-1, 0, 1, 2, -1, -4]
    print(Solution().threeSum(nums))