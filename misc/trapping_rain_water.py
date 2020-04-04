"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png
"""

class Solution:
    def trap(self, height):
        n = len(height)
        l, r = 0, n-1
        res = 0
        while l < r:
            if height[l] < height[r]:
                max_h = height[l]
                l += 1
                while l < r and height[l] < max_h:
                    res += max_h - height[l]
                    l += 1
            else:
                max_h = height[r]
                r -= 1
                while l < r and height[r] < max_h:
                    res += max_h - height[r]
                    r -= 1
        return res


def main():
    assert Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6


if __name__ == '__main__':
    main()