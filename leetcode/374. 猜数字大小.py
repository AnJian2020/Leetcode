# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        lower,heigh=1,n
        while lower<=heigh:
            middle=int((heigh-lower)/2)+lower
            tmp=guess(middle)
            if tmp==0:
                return middle
            elif tmp==-1:
                heigh=middle-1
            elif tmp==1:
                lower=middle+1
        return -1
