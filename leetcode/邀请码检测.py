# -*- coding:utf-8 -*-
"""
time: 2020/6/18
author: xuhao
"""

class Solution:
    def checkInvitationCode(self,invitationCode):
        if len(invitationCode) > 16 or len(invitationCode) < 16:
            return 'error'
        invitationCode =  list(invitationCode)
        invitationCodeLength = len(invitationCode)
        evenNumberSum,oddNumberSum,item = 0,0,invitationCodeLength-1
        #evenNumberSum为偶数位和,oddNumberSum为奇数位和
        while item >= 0:
            if (item+1)%2 == 1:     #奇数和
                if invitationCode[item].isdigit():
                    oddNumberSum+=int(invitationCode[item])
                else:
                    oddNumberSum+=ord(invitationCode[item])%96%9
            elif (item+1)%2 == 0:       #偶数和
                if invitationCode[item].isdigit():
                    oddSum = int(invitationCode[item])*2
                else:
                    oddSum=ord(invitationCode[item])%96%9*2
                if oddSum>9:
                    oddSum -= 9
                evenNumberSum+=oddSum
            item-=1
        if (evenNumberSum+oddNumberSum)%10 == 0:
            return 'ok'
        else:
            return 'error'


if __name__=="__main__":
    print(Solution().checkInvitationCode('11111111111b3211'))
