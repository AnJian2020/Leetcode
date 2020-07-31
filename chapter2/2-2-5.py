

def deleteValue(numList,s:int,t:int):
    k=0
    if s>=t or len(numList)==0:
        return False
    for item in range(len(numList)):
        if numList[item]>=s and numList[item]<=t:
            k+=1
        else:
            numList[item-k]=numList[item]
    while k>0:
        numList.pop()
        k-=1


if __name__=="__main__":
    nums=[1,2,3,4,5,6,7,8,9]
    deleteValue(nums,3,6)
    print(nums)
