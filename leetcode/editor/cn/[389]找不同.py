# 给定两个字符串 s 和 t，它们只包含小写字母。 
# 
#  字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。 
# 
#  请找出在 t 中被添加的字母。 
# 
#  
# 
#  示例: 
# 
#  输入：
# s = "abcd"
# t = "abcde"
# 
# 输出：
# e
# 
# 解释：
# 'e' 是那个被添加的字母。
#  
#  Related Topics 位运算 哈希表 
#  👍 155 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import collections
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_count=collections.Counter(s)
        t_count=collections.Counter(t)
        for item in t:
            if t_count.get(item,0)-s_count.get(item,0)>0:
                return item
        return

# leetcode submit region end(Prohibit modification and deletion)
