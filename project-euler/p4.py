#!/usr/bin/python

def strrev (num):
    j = str(num)
    k = len(str(num))-1
    l = list(j)
    for i in range(0,k+1):
        l[i] = j[k-i]
    w = "".join(l)
    return w


digitmax = 999
maxnum = digitmax
multiplier = digitmax
maxpal = 0
for i in range(1,maxnum+1):
    while multiplier > 0:
        num = digitmax*multiplier
        revnum = strrev(num)
        if str(revnum) == str(num):
            if num > maxpal:
                maxpal = num
        multiplier = multiplier-1
    multiplier =  maxnum
    digitmax = digitmax - i
print maxpal
