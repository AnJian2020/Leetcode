class Solution:
    def reverse(self, x: int) -> int:
        if x >2147483647 or x < -2147483648:
            return 0
        else:
            num=list(str(x))
            result=""
            if num[0]=="-":
                result="-"
                num.pop(0)
            l=0
            while l<len(num):
                if num[-1] == "0":
                    num.pop(-1)
                l+=1
            if len(num)==0:
                return 0
            i=len(num)-1
            while i>=0:
                result=result+num[i]
                i-=1
            if int(result) > 2**31 or int(result) < -2**31-1:
                return 0
            else:
                return int(result)

if __name__=="__main__":

    print(Solution().reverse(1534236469))
