from typing import List

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        for item in range(len(A)):
            A[item]=A[item]**2
        return sorted(A)

if __name__=="__main__":
    print(Solution().sortedSquares([-7,-3,2,3,11]))


