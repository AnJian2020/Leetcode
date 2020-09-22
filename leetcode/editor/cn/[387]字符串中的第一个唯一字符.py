# 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。 
# 
#  
# 
#  示例： 
# 
#  s = "leetcode"
# 返回 0
# 
# s = "loveleetcode"
# 返回 2
#  
# 
#  
# 
#  提示：你可以假定该字符串只包含小写字母。 
#  Related Topics 哈希表 字符串 
#  👍 269 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

import collections

class Solution:
    def firstUniqChar(self, s: str) -> int:

        count=collections.Counter(s)
        for item in range(len(s)):
            if count[s[item]]==1:
                return item
        return -1
# leetcode submit region end(Prohibit modification and deletion)
