class Solution:
    def isUnique(self, astr: str) -> bool:
        result=True
        item=0
        while item<len(astr)-1:
            j=item+1
            while j<len(astr):
                if astr[item]==astr[j]:
                    result=False
                    break
                j+=1
            item+=1
        return  result

if __name__=="__main__":
    astr=""
    print(Solution().isUnique(astr))