# -*- coding:utf-8 -*-
# author:许浩

from typing import List

class SortList:
    def __init__(self,numList:List,MaxSize=50):
        self.numList=numList
        self.MaxSiae=MaxSize

    def ListInsert(self,i:int,e:int)->bool:
        if i<1 or i>len(self.numList)+1:
            return False
        if i>self.MaxSiae:
            return False
        self.numList.append(None)
        item=len(self.numList)-1
        while item>=i:
            self.numList[item]=self.numList[item-1]
            item-=1
        self.numList[i-1]=e
        return True

    def ListDelete(self,i:int)->bool:
        if i<1 or i>len(self.numList)+1:
            return False
        length=len(self.numList)
        j=i
        while j<length:
            self.numList[j-1]=self.numList[j]
            j+=1
        return True

    def LocateElem(self,e:int)->int:
        for item in range(len(self.numList)):
            if self.numList[item]==e:
                return item+1
        return 0


