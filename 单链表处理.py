# -*- coding:utf-8 -*-
"""
time: 2020/6/18
author: xuhao
"""
from typing import List


class Solution:
    def sortNumber(self,numList1:List,numList2:List):
        result=[None for i in range(len(numList2))]
        numListTemp1=numList1
        numListTemp2=numList2
        for item in range(1,len(numList1)):
            maxIndex1=numListTemp1.index(max(numListTemp1))
            maxIndex2=numListTemp2.index(max(numListTemp2))
            maxVaule=max(numListTemp2)
            numListTemp2.pop(maxIndex2)
            numListTemp1.pop(maxIndex1)
            result[maxIndex1]=maxVaule
        for item1 in range(len(result)):
            if result[item1]==None:
                result[item1]=numListTemp2[-1]
        return result

    def sortNumber1(self,numList1,numList2):
        count={}
        for item1 in range(len(numList1)-1):
            for item2 in range(item1+1,len(numList1)):
                if abs(numList1[item1]-numList1[item2]) in count.keys():
                    count[abs(numList1[item1]-numList1[item2])] += 1
                else:
                    count[abs(numList1[item1] - numList1[item2])] = 1

        print(count)


if __name__=="__main__":
    print(Solution().sortNumber1([5,7,4,9],[1,2,3,4]))