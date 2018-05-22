#!/usr/bin/env python3

import math

class Solution:
  def countPrimes(self, n):
    a = [True] * n
    for i in range(2,math.ceil(math.sqrt(n))):
      if a[i]:
        iter = 0
        j = i**2
        while j < n:
          a[j] = False
          j = (i**2)+(i*iter)
          iter += 1

    return a[2:].count(True)

if __name__ == "__main__":
  count = Solution()
  print(count.countPrimes(1500000))
