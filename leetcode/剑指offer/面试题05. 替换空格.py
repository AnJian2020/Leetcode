from builtins import str
class Solution:
    def replaceSpace(self, s: str) -> str:
        return s.replace(" ","%20")

if __name__=="__main__":
    str="We are happy."
    print(Solution().replaceSpace(str))