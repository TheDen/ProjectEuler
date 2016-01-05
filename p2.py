#!/usr/bin/python

j=1
k = 1
fib = 1
sum = 0
while fib <= 4000000:
    j = k
    k = fib
    fib = k + j
    if fib%2==0:
       sum = sum + fib
print sum
    
