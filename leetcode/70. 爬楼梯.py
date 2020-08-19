class Solution:
    def climbStairs(self, n: int) -> int:
        # def f(x):
        #     result=1
        #     for i in range(1,x+1):
        #         result=result*i
        #     return result
        # count=0
        # if n%2==0:
        #     tmp=int(n/2)
        #     for i in range(tmp+1):    #i为2的次数
        #         count+=f(n-i)/(f(i)*f(n-2*i))
        # elif n%2==1:
        #     tmp = int((n-1) / 2)
        #     for i in range(tmp + 1):  # i为2的次数
        #         count += f(n- i) / (f(i) * f(n -2 * i))
        # return int(count)
        import math
        a=math.sqrt(5)
        f=math.pow((1+a)/2,n+1)-math.pow((1-a)/2,n+1)
        return int(f/a)

if __name__=="__main__":
    print(Solution().climbStairs(3))


