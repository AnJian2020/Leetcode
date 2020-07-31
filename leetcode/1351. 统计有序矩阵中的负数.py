from typing import List

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count=0
        for item in grid:
            item.sort()
            i=0
            while i<len(item):
                if item[i]<0:
                    count+=1
                else:
                    break
                i+=1
        return count

if __name__=="__main__":
    grid = [[-1]]
    print(Solution().countNegatives(grid))