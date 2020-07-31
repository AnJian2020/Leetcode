class SeqList:
    def __init__(self,data,MaxSize,length):
        self.data=data
        self.MaxSize=MaxSize
        self.length=length

class Solution:
    def removeList(self,L:SeqList):
        count=int(L.length/2)
        for item in range(count):
            temp=L.data[item]
            L.data[item]=L.data[L.length-item-1]
            L.data[L.length-item-1]=temp
        return L

if __name__=="__main__":
    num=SeqList([1,2,3,4,5],12,5)
    print(Solution().removeList(num).data)
