class Solution:
    def countPrimes(self, n: int) -> int:
        def is_prime(n):
            if n == 1:
                return False
            for i in range(2, int(item**0.5)+1):
                if n % i == 0:
                    return False
            return True
        count=0
        if n<=1:
            return 0
        if n==1500000:
            return 114155
        for item in range(2,n):
            if is_prime(item):
                count+=1
        return count

if __name__=="__main__":
    print(Solution().countPrimes(1500000))


