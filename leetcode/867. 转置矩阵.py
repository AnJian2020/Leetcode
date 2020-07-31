from typing import List


class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        result=[]
        for i in range(len(A[0])):
            num = []
            for item in A:
                num.append(item[i])
            result.append(num)
        return result

if __name__=="__main__":
    A=[[1,2,3],[4,5,6]]
    print(Solution().transpose(A))
