# -*- coding:utf-8 -*-

# author: xuhao

# @Time: 2020/4/26

def getNext(patternString):
    next=[0]*(len(patternString)+1)
    i,j=1,0
    while i<len(patternString):
        if j==0 or patternString[i]==patternString[j]:
            i+=1
            j+=1
            next[i]=j
        else:
            j=next[j]
    return next

def getIndex(patternString,mainString,next):
    i,j=1,1
    while i<len(mainString) and j<len(patternString):
        if j==0 or mainString[i]==patternString[j]:
            i+=1
            j+=1
        else:
            j=next[j]
    if j>=len(patternString):
        return i-len(patternString)
    else:
        return -1

mainString='bdhbhabadjhahd'
patternString='abva'
print(mainString.find(patternString))