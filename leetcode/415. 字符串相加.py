class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i,j=len(num1)-1,len(num2)-1
        result=''
        carray=0
        while i>=0 or j>=0:
            tmp1=int(num1[i]) if i>=0 else 0
            tmp2=int(num2[j]) if j>=0 else 0
            tmp=tmp1+tmp2+carray
            if tmp>=10:
                carray=1
            else:
                carray=0
            result+=str(tmp%10)
            i-=1
            j-=1
        if carray==1:
            result+='1'
        return result[::-1]

if __name__=="__main__":
    print(Solution().addStrings('9','1'))