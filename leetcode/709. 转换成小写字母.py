class Solution:
    def toLowerCase(self, str: str) -> str:
        result=""
        strList=list(str)
        print(ord("a"))
        print(ord("Z"))
        for item in strList:
            if ord(item)>=65 and ord(item)<=90:
                result+=chr(ord(item)+32)
            else:
                result+=item

        return result
if __name__=="__main__":
    print(Solution().toLowerCase("HELL&O"))