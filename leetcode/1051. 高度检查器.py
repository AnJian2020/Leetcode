from typing import List

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count=0
        nowHights=sorted(heights)
        for item in range(len(heights)):
            if heights[item]!=nowHights[item]:
                count+=1
        return count

if __name__=="__main__":
    heights=[1,1,4,2,1,3]
    print(Solution().heightChecker(heights))

