#!/usr/bin/env python3


class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        list = [str(i) for i in str(x)][::-1]
        if list[-1] == "-":
            list = ["-"] + list
            list.pop()
        while list[0] == "0":
            list.pop(0)
        reversed_integer = int("".join(list))
        if reversed_integer < 0:
            if -0x80000000 != reversed_integer & -0x80000000:
                return 0
        elif reversed_integer > 0:
            if reversed_integer != reversed_integer & 0x7FFFFFFF:
                return 0
        return reversed_integer


if __name__ == "__main__":
    nums = [123, -123, 120, 0, 1534236469, -2147483412]
    target = 0
    soln = Solution()
    for i in nums:
        print(soln.reverse(i))
