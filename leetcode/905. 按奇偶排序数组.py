from typing import List


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        result=[]
        for item in A:
            if item%2==0:
                result=[item]+result
            else:
                result.append(item)
        return result

if __name__=="__main__":
    A=[3,1,2,4]
    print(Solution().sortArrayByParity(A))


