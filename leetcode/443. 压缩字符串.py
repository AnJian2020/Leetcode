from typing import List
import collections

# class Solution:
#     def compress(self, chars: List[str]) -> int:
#
#         charsNum=dict(collections.Counter(chars))
#         result=[]
#         for key,value in charsNum.items():
#             if value<=1:
#                 result.append(key)
#             else:
#                 result.append(key)
#                 result.extend([item for item in str(value)])
#         return result

class Solution(object):
    def compress(self, chars):
        anchor = write = 0
        for read, c in enumerate(chars):
            if read + 1 == len(chars) or chars[read + 1] != c:
                chars[write] = chars[anchor]
                write += 1
                if read > anchor:
                    for digit in str(read - anchor + 1):
                        chars[write] = digit
                        write += 1
                anchor = read + 1
        return write



if __name__=="__main__":
    print(Solution().compress(["a","a","b","b","c","c","c"]))
