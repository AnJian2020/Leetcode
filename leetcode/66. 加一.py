from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        tmp=0
        item=len(digits)-1
        while item>=0:
            tmp+=digits[item]*10**(len(digits)-item-1)
            item-=1
        tmp+=1
        result=[]
        for i in str(tmp):
            result.append(int(i))
        return result

if __name__=="__main__":
    d=[1,0,9]
    print(Solution().plusOne(d))
