
class Solution:
    def printNumbers(self, n):    
        numLen=1
        result=[]
        while n>0:
            numLen*=10
            n-=1
        for item in range(1,numLen):
            result.append(item)
        return result

if __name__ == "__main__":
    print(Solution().printNumbers(33))
