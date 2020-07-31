from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result=[]
        for item1 in nums1:
            for item2 in nums2:
                if item1==item2:
                    result.append(item1)
        result=list(set(result))
        return result

if __name__=="__main__":
    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    print(Solution().intersection(nums1,nums2))