from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1.sort()
        numcount={}
        result=[]
        for item in arr2:
            numcount[item]=arr1.count(item)
            i=0
            while i<arr1.count(item):
                result.append(item)
                i+=1
        for item in arr1:
            if item not in arr2:
                result.append(item)
        print(result)

if __name__=="__main__":
    arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
    arr2 = [2, 1, 4, 3, 9, 6]
    Solution().relativeSortArray(arr1,arr2)
