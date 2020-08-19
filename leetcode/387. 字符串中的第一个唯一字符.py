import collections
class Solution:
    def firstUniqChar(self, s: str) -> int:
        sNum=dict(collections.Counter(s))
        for item in range(len(s)):
            if sNum[s[item]]==1:
                return item
        return -1

if __name__=="__main__":
    print(Solution().firstUniqChar('loveleetcode'))