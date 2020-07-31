class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        return sorted(s1)==sorted(s2)

if __name__=="__main__":
    print(Solution().CheckPermutation(s1 = "abc", s2 = "bca"))