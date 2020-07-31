from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i=0
        while i<n:
            nums1[m+i]=nums2[i]
            i+=1
        nums1.sort()

if __name__=="__main__":
    nums1=[1,2,3,0,0,0]
    nums2=[4,5,6]
    Solution().merge(nums1,3,nums2,3)
    print(nums1)