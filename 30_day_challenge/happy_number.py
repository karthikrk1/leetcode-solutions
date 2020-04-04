"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer,
replace the number by the sum of the squares of its digits, and repeat the process until the number
equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy numbers.

Example:
Input: 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""

class Solution:
    def isHappy(self, n):
        seen = set()
        while True:
            if n in seen:
                break
            else:
                seen.add(n)
                val = 0
                while n > 0:
                    val += (n%10)**2
                    n //= 10
                n = val
        return n == 1


def main():
    solution = Solution()
    case_1 = solution.isHappy(19)
    assert case_1
    case_2 = solution.isHappy(2)
    assert not case_2


if __name__ == "__main__":
    main()