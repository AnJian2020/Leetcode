# -*- coding:utf-8 -*-
"""
time: 2020/6/18
author: xuhao
"""

class Solution:
    def getNumber(self):
        result=[]
        for item1 in range(10,100):
            for item2 in range(10,100):
                itemlist1=list(str(item1))
                itemlist2=list(str(item2))
                if int(itemlist1[0])*int(itemlist2[0])==int(itemlist1[1])*int(itemlist2[1]):
                    result.append([item1,item2])
        return result
