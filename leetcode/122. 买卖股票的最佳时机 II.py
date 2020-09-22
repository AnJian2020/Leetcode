from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # maxprofit=0
        # for item in range(1,len(prices)):
        #     if prices[item]>prices[item-1]:
        #         maxprofit+=prices[item]-prices[item-1]
        # return maxprofit
        peak= prices[0]
        valley = prices[0]
        maxprofit,item=0,0
        while item<len(prices)-1:
            while item<len(prices)-1 and prices[item]>=prices[item+1]:
                item+=1
            valley=prices[item]
            while item<len(prices)-1 and prices[item]<prices[item+1]:
                item+=1
            peak=prices[item]
            maxprofit+=peak-valley
        return maxprofit



if __name__=="__main__":
    prices=[7,1,5,3,6,4]
    print(Solution().maxProfit(prices))