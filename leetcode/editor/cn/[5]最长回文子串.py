# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。 
# 
#  示例 1： 
# 
#  输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
#  
# 
#  示例 2： 
# 
#  输入: "cbbd"
# 输出: "bb"
#  
#  Related Topics 字符串 动态规划 
#  👍 2717 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return s
        elif len(s) == 1 or (len(s) == 2 and s[1] != s[0]):
            return s[0]
        elif len(s) == 2 and s[0] == s[1]:
            return s
        start=0
        result=''
        while start<len(s)-1:
            end=start+1
            tmp=s[start]
            while end<len(s):
                tmp+=s[end]
                if tmp==tmp[::-1]:
                    result=tmp if len(tmp)>len(result) else result
                end+=1
            start+=1
        if len(result)==0:
            return s[0]
        return result

# leetcode submit region end(Prohibit modification and deletion)
