from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        index1,index2=0,0
        result=[]
        while index1<len(nums1) and index2<len(nums2):
            if nums1[index1]<nums2[index2]:
                index1+=1
            elif nums1[index1]==nums2[index2]:
                result.append(nums1[index1])
                index1+=1
                index2+=1
            else:
                index2+=1
        return result