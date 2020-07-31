
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_list=list(s)
        t_list=list(t)
        s_list.sort()
        t_list.sort()
        if t_list==s_list:
            return True
        else:
            return False

if __name__=="__main__":
    s="anagram"
    t="nagaram"
    print(Solution().isAnagram(s,t))