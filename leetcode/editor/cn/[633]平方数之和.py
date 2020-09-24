# 给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a2 + b2 = c。 
# 
#  示例1: 
# 
#  
# 输入: 5
# 输出: True
# 解释: 1 * 1 + 2 * 2 = 5
#  
# 
#  
# 
#  示例2: 
# 
#  
# 输入: 3
# 输出: False
#  
#  Related Topics 数学 
#  👍 142 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a=0
        while a**2<=c:
            b=(c-a**2)**0.5
            if b-int(b)==0:
                return True
            a+=1
        return False


# leetcode submit region end(Prohibit modification and deletion)
