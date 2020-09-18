# -*- coding:utf-8 -*-
"""
time: 2020/6/18
author: xuhao
"""

class Solution:
    def distributeGameMoneyOne(self,n:int,sum:int):
        """
        暴力方法，效率比低
        """
        faceValue=[1,2,5,10]
        result=[]
        for item1 in range(n+1):
            for item2 in range(n+1-item1):
                for item3 in range(n+1-item1-item2):
                    for item4 in range(n+1-item1-item2-item3):
                        if sum==item1*faceValue[0]+item2*faceValue[1]+\
                                item3*faceValue[2]+item4*faceValue[3]:
                            result.append([item1,item2,item3,item4])
        return result

if __name__=="__main__":
    print(Solution().distributeGameMoneyOne(9,100))



