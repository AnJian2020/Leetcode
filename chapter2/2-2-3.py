class SeqList:
    def __init__(self,data,length):
        self.data=data
        self.length=length
        
class Solution:
    def deleteValue(self,x:int,num:SeqList):
        count=0
        for item in range(num.length):
            if num.data[item]!=x:
                num.data[count]=num.data[item]
                count+=1
        num.length=count

if __name__=="__main__":
    num=SeqList([1,2,3,4,5,3,2,6],8)
    Solution().deleteValue(2,num)
    print(num.data)