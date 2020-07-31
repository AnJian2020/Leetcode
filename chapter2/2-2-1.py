from typing import List

class SeqList:
    def __init__(self,data,MaxSize,length):
        self.data=data
        self.MaxSize=MaxSize
        self.length=length
        

class Solution(object):
    def deleteMinValue(self,L:SeqList)->int:
        if L.length==0:
            return -1
        minIndex=0
        value=L.data[0]
        for item in range(1,L.length):
            if L.data[item]<L.data[minIndex]:
                value=L.data[item]
                minIndex=item

        L.data[minIndex]=L.data[-1]
        L.length-=1
        return value

if __name__=="__main__":
    num=SeqList([2,3,4,1,5,3],12,6)
    print(Solution().deleteMinValue(num))
    
    




