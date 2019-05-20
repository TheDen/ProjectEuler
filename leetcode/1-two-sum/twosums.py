#!/usr/bin/env python3


class Solution:
    def twoSum(self, nums, target):
        nums
        soln = []
        sortedarray = sorted(nums)
        for idx1, i in enumerate(sortedarray):
            for idx2, j in enumerate(sortedarray):
                if (i + j) == target:
                    if i == j:
                        first = nums.index(i)
                        second = nums.index(j, first + 1)
                        return [first, second]
                    else:
                        return [nums.index(i), nums.index(j)]


if __name__ == "__main__":
    nums = [0, 4, 3, 0]
    target = 0
    soln = Solution()
    print(soln.twoSum(nums, target))
