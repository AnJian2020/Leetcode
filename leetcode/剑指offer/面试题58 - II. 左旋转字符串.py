class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        return s[n:]+s[:n]

if __name__=="__main__":
    print(Solution().reverseLeftWords("lrloseumgh", 6))
