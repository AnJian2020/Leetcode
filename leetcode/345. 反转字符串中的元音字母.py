class Solution:
    def reverseVowels(self, s: str) -> str:
        yuan=['a','e','i','o','u','A','E','I','O','U']
        strList=[item for item in s]
        i,j=0,len(strList)-1
        while i<j:
            if strList[i] in yuan and strList[j] in yuan:
                tmp=strList[i]
                strList[i]=strList[j]
                strList[j]=tmp
                i+=1
                j-=1
            elif strList[i] not in yuan and strList[j] in yuan:
                i+=1
            elif strList[i] in yuan and strList[j] not in yuan:
                j-=1
            else:
                i+=1
                j-=1
        return ''.join(strList)


if __name__=="__main__":
    print(Solution().reverseVowels("ai"))
