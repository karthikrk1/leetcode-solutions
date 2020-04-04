"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest
sum and return its sum.

Example:
    Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""

class Solution:
    def max_sub_array(self, nums):
        max_sum = float('-inf')
        curr = 0
        for i in nums:
            curr = max(i, curr + i)
            max_sum = max(max_sum, curr)
        return max_sum


def main():
    soln = Solution()
    case_1 = soln.max_sub_array([-2,1,-3,4,-1,2,1,-5,4])
    assert case_1 == 6


if __name__ == "__main__":
    main()