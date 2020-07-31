class SeqList:
    def __init__(self,data,length):
        self.data=data[:length]
        self.length=length

def deleteRangeValue(numList:SeqList,s:int,t:int)->bool:
    if s>=t or numList.length==0:
        return False

    for i in range(numList.length):
        if numList.data[i]>s:
            break
    for j in range(i,numList.length):
        if numList.data[j]>t:
            break
    while j<numList.length:
        numList.data[i]=numList.data[j]
        j+=1
        i+=1
    numList=SeqList(numList.data,i)
    return True

if __name__ == "__main__":
    numList=SeqList([1,2,3,4,5,6,7,8],8)
    if deleteRangeValue(numList,2,4):
        print(numList.length)
    
    







