class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if s=="" or s==" ":
            return 0
        strlist=s.split(" ")
        i=len(strlist)-1
        while i>=0:
            if strlist[i]=="":
                strlist.pop(i)
            i-=1
        if len(strlist)==0:
            return  0
        else:
            return  len(strlist[-1])

if __name__=="__main__":
    print(Solution().lengthOfLastWord("        "))