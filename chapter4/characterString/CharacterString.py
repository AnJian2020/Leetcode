# -*- coding:utf-8 -*-
import copy
class CharacterString(object):

    #=是赋值，两者的地址不同
    def strAssign(self,T):
        S=T
        return S

    #copy两者地址相同
    def strCopy(self,S):
        T=copy.copy(S)
        return T

    def strEmpty(self,S):
        return len(S)==0

    def strLength(self,S):
        return len(S)

    def subString(self,s,pos,strlen):
        if pos>len(s) or pos+strlen>len(s):
            return -1
        return s[pos-1:pos+strlen]

    def concat(self,s1,s2):
        return s1+s2

    def Index(self,s,t):
        s,t=list(s),list(t)
        i,j=0,0
        while i<len(s) and j<len(t):
            if s[i]==t[j]:
                i+=1
                j+=1
            else:
                i=i-j+1
                j=0
        if j+1>len(t):
            return i-len(t)
        else:
            return 0

    def clearString(self,s):
        return ''

    def destoryString(self,s):
        del s










