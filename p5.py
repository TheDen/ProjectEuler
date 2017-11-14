#!/usr/bin/python

num = 380
#div=[2,3,5,7,8,9]
div=[7,8,9,11,13,16,17]
div = div[::-1]
alen = len(div)
j = 0
k = 0
while True:
    for i in range(0,alen):
        if num%div[i]==0:
            j = j+1
        else:
            break
        if j == alen:
            print num
            break
        j = 0
        num = num+380
