from typing import List

"""
将第一个字符串在列表中查找是否有公共的，循环截取最后一个字符
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0:
            return ""
        result=strs[0]
        i=1
        while i<len(strs):
            while strs[i].find(result)!=0:
                result=result[:-1]
            i+=1
        return result



if __name__=="__main__":
    print(Solution().longestCommonPrefix(["dog","racecar","car"]))