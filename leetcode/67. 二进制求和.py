class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num1=int(a,base=2)
        num2=int(b,base=2)
        return bin(num2+num1).replace("0b","")

if __name__=="__main__":
    print(Solution().addBinary(a = "11", b = "1"))