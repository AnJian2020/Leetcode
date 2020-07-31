from typing import List
class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix)==0 or len(matrix[0])==0:
            return False
        for item1 in matrix:
            if item1[0]<=target and item1[-1]>=target:
                for item2 in item1:
                    if target==item2:
                        return True
        return False