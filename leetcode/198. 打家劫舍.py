from typing import List
"""
用 dp[i]dp[i] 表示前 ii 间房屋能偷窃到的最高总金额，那么就有如下的状态转移方程：

\textit{dp}[i] = \max(\textit{dp}[i-2]+\textit{nums}[i], \textit{dp}[i-1])
dp[i]=max(dp[i−2]+nums[i],dp[i−1])

边界条件为：

\begin{cases} \textit{dp}[0] = \textit{nums}[0] & 只有一间房屋，则偷窃该房屋 \\ \textit{dp}[1] = \max(\textit{nums}[0], \textit{nums}[1]) & 只有两间房屋，选择其中金额较高的房屋进行偷窃 \end{cases}
{ 
dp[0]=nums[0]
dp[1]=max(nums[0],nums[1])
​	
  
只有一间房屋，则偷窃该房屋
只有两间房屋，选择其中金额较高的房屋进行偷窃
​	
 

最终的答案即为 \textit{dp}[n-1]dp[n−1]，其中 nn 是数组的长度。

"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        first,second=nums[0],max(nums[1],nums[0])
        for item in range(2,len(nums)):
            first,second=second,max(nums[item]+first,second)
        return second

if __name__=="__main__":
    nums=[2,7,9,3,1]
    print(Solution().rob(nums))
