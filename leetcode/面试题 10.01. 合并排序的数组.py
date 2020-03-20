from typing import List


class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        """
        Do not return anything, modify A in-place instead.
        """
        A[m:]=B
        A.sort()

if __name__=="__main__":
    A = [1, 2, 3, 0, 0, 0,0]
    B = [2, 5, 6,4]
    Solution().merge(A,3,B,3)
    print(A)