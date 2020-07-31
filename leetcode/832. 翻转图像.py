from typing import List

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for item_1 in range(len(A)):
            A[item_1].reverse()
            for item_2 in range(len(A[item_1])):
                if A[item_1][item_2]==0:
                    A[item_1][item_2]=1
                elif A[item_1][item_2]==1:
                    A[item_1][item_2]=0
        return A


if __name__=="__main__":
    A=[[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
    print(Solution().flipAndInvertImage(A))

