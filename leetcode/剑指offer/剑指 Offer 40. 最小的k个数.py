from typing import List


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        return arr[0:k]

if __name__=="__main__":
    print(Solution().getLeastNumbers([0,1,2,1],1))
