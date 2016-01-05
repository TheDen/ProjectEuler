#!/usr/bin/python

j = 0
for  i in range(1,1000):
    if i%3==0:
        j = j+i
    elif i%5==0:
        j = j+i
        
    # print '%d' % i
    
print j
