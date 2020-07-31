"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
"""
class Solution:
    def twoSum(self, List,numsum):
        lens = len(List)
        j=-1
        for i in range(1,lens):
            temp = List[:i]
            if (numsum - List[i]) in temp:
                j = temp.index(numsum - List[i])
                break
        if j>=0:
            return [j,i]

if __name__=="__main__":
    List=[2,3,4,5,1]
    numsum=7
    print(Solution().twoSum(List,numsum))