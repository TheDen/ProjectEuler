#!/usr/bin/python

import math

sumsquares = 0
sqauresum = 0
for i in range(1,101):
    sumsquares += math.pow(i,2)
    sqauresum += i

result = math.pow(sqauresum,2) - sumsquares

print result
