from typing import List


class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        # 滑动窗口
        # def sumRange(small:int,big:int):
        #     sum=0
        #     for item in range(small,big+1):
        #         sum+=item
        #     return sum
        # small,big=1,2
        # middle=int(target/2)
        # result=[]
        # while small<=middle:
        #     sum=sumRange(small,big)
        #     if sum<target:
        #         big+=1
        #     elif sum>target:
        #         small+=1
        #     else:
        #         result.append([item for item in range(small,big+1)])
        #         big+=1
        # return result
        # 求根法
        #
        # 间隔法
        item,result=1,[]
        while item*(item+1)/2<target:
            x=(target-item*(1+item)/2)/(item+1)
            if x-int(x)==0:
                result.append(list(range(int(x),int(x)+item+1)))
            item+=1
        return result[::-1]





if __name__=="__main__":
    target=9
    print(Solution().findContinuousSequence(target))