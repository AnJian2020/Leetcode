class Solution:
    def titleToNumber(self, s: str) -> int:
        strList=list(s)
        length=len(strList)
        result=0
        item=length-1
        count=0
        while item>=0:
            result=result+(ord(strList[item])-64)*(26**count)
            count+=1
            item-=1
        return result


if __name__=="__main__":
    print(Solution().titleToNumber("A"))