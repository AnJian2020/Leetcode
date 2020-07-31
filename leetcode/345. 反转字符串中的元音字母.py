class Solution:
    def reverseVowels(self, s: str) -> str:

        def isOrigin(s):
            if s=="a" or s=='e' or s=='i' or \
                    s=="o" or s=='u' or s=='A' or \
                    s=="E" or s==['I'] or s=="O" or \
                    s=="U":
                return True
            else:
                return False

        strList=s
        print(strList)
        i,j=0,len(strList)-1
        while i<j:
            if not isOrigin(strList[i]):
                i+=1
                continue
            if not isOrigin(strList[j]):
                j-=1
                continue
            tem=strList[i]
            strList[i]=strList[j]
            strList[j]=tem
            i+=1
            j-=1
        result=''
        for item in strList:
            result+=item
        return result

if __name__=="__main__":
    print(Solution().reverseVowels("Live on evasions? No, I save no evil."))
