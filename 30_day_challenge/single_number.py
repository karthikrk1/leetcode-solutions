"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Input: [2,2,1]
Output: 1

Input: [4,1,2,1,2]
Output: 4
"""

class Solution:
    def single_number(self, nums):
        xor = 0
        for i in nums:
            xor ^= i
        return xor


def main():
    solution = Solution()
    case_1 = solution.single_number([2,2,1])
    print("First case output: " + str(case_1))
    assert case_1 == 1
    case_2 = solution.single_number([4,1,2,1,2])
    print("Second case output: " + str(case_2))
    assert  case_2 == 4


if __name__ == "__main__":
    main()