class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return n%1000000007
        elif n==1:
            return n%1000000007
        fitone=0
        fittwo=1
        fitn=0
        i=2
        while i<=n:
            fitn=fitone+fittwo
            fittwo=fitone
            fitone=fitn
            i+=1
        return i%1000000007