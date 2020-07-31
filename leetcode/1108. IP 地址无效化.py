class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".",'[.]')

if __name__=="__main__":
    print(Solution().defangIPaddr("255.100.50.0"))
