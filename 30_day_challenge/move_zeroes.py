"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of
the non-zero elements.

Example:
    Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

Note:
    Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""

class Solution:
    def move_zeroes(self, nums):
        """
        Doesn't return modifies the array inplace
        :param nums: an array of integers
        :return: None
        """
        ptr2 = 0
        for ptr1 in range(len(nums)):
            if nums[ptr1] != 0:
                nums[ptr2] = nums[ptr1]
                ptr2 += 1
        while ptr2 < len(nums):
            nums[ptr2] = 0
            ptr2 += 1


def main():
    soln = Solution()
    nums = [0,1,0,3,12]
    soln.move_zeroes(nums)
    assert nums == [1,3,12,0,0]


if __name__ == "__main__":
    main()