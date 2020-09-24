# 给定一个范围在 1 ≤ a[i] ≤ n ( n = 数组大小 ) 的 整型数组，数组中的元素一些出现了两次，另一些只出现一次。 
# 
#  找到所有在 [1, n] 范围之间没有出现在数组中的数字。 
# 
#  您能在不使用额外空间且时间复杂度为O(n)的情况下完成这个任务吗? 你可以假定返回的数组不算在额外空间内。 
# 
#  示例: 
# 
#  
# 输入:
# [4,3,2,7,8,2,3,1]
# 
# 输出:
# [5,6]
#  
#  Related Topics 数组 
#  👍 462 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import copy


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # maxNumber = len(nums)
        # result = []
        # for item in range(1, maxNumber + 1):
        #     if item not in nums:
        #         result.append(item)
        # return result
        numberList = copy.copy(nums)
        for item in nums:
            if numberList[item - 1] > 0:
                numberList[item - 1] = -(numberList[item - 1])
        return [item + 1 for item in range(len(numberList)) if numberList[item] > 0]
# leetcode submit region end(Prohibit modification and deletion)
