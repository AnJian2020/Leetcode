class Solution:
    def romanToInt(self, s: str) -> int:
        num0={"I":1,"V":5, "X":10,"L":50,"C":100,"D":500,"M":1000,"IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900}
        numstr=list(s)
        print(numstr)
        result=0
        i=0
        num1=[]
        while i<len(numstr):
            if i+1<len(numstr) and numstr[i]+numstr[i+1] in list(num0.keys()):
                result=result+num0[numstr[i]+numstr[i+1]]
                num1.append(numstr[i]+numstr[i+1])
                i+=2
            else:
                result=result+num0[numstr[i]]
                num1.append(numstr[i])
                i+=1
        print(num1)
        return result

if __name__=="__main__":
    print(Solution().romanToInt("MCDLXXVI"))