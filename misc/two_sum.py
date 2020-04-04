"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

class Solution:
    def two_sum(self, nums, target):
        d = {}
        for i, v in enumerate(nums):
            if (target - v) in d:
                return [d[target-v], i]
            else:
                d[v] = i


def main():
    sol = Solution()
    assert sol.two_sum([2, 7, 11, 15], 9) == [0,1]


if __name__ == "__main__":
    main()