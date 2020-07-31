class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        numList=list(str(n))
        sum=0
        product=1
        for item in range(len(numList)):
            numList[item]=int(numList[item])
            sum+=numList[item]
            product*=numList[item]
        result=product-sum

        return result

if __name__ == "__main__":
    print(Solution().subtractProductAndSum(4421))