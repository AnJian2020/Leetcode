class Solution(object):
    def reverseWords(self, s: str) -> str:
        return  ' '.join(reversed(s.split()))

if __name__=="__main__":
    print(Solution().reverseWords("a good   example"))