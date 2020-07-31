from typing import List

class Solution:
    def addList(self,numList1:List,numList2:List)->List:
        result=[]
        i,j=0,0
        while i<len(numList1) and j<len(numList2):
            if numList1[i]<=numList2[j]:
                result.append(numList1[i])
                i+=1
            else:
                result.append(numList2[j])
                j+=1
        while i<len(numList1):
            result.append(numList1[i])
            i+=1
        while j<len(numList2):
            result.append(numList2[j])
            j+=1
        return result

if __name__=="__main__":
    num1=[1,2,3,4,5,6,7]
    num2=[2,3,4,5,6,7,8]
    print(Solution().addList(num1,num2))
