
"""
因为 Excel 取值范围为 1~26，故可将 26 进制 逻辑上的 个位、十位、百位…均减 1 映射到 0~25 即可，
最后转换为字符
"""
class Solution:
    def convertToTitle(self, n: int) -> str:
        result=''
        while n!=0:
            n-=1
            result+=chr(ord('A') + n % 26)
            n=int(n/26)
        return result[::-1]


if __name__=="__main__":
    print(Solution().convertToTitle(28))
