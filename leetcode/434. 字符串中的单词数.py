class Solution:
    def countSegments(self, s: str) -> int:
        if s == '':
            return 0
        strlist=s.split(" ")
        result=[]
        for item in strlist:
            if item!='':
                result.append(item)
        return len(result)

if __name__=="__main__":
    print(Solution().countSegments("                "))