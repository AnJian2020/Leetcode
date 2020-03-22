class Solution:
    def maximum69Number (self, num: int) -> int:

        numList=list(str(num))
        for item in range(len(numList)):
            if numList[item]=="6":
                numList[item]="9"
                break
        result=''
        for item in numList:
            result+=item
        return int(result)

if __name__=="__main__":
    print(Solution().maximum69Number(1661))