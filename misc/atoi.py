"""
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.


Input: "42"
Output: 42

Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.

Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.

Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical
             digit or a +/- sign. Therefore no valid conversion could be performed.

Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Thefore INT_MIN (−231) is returned.
"""

class Solution:
    def atoi(self, s):
        MAX_INT = 2147483647
        MIN_INT = -2147483648
        s = s.strip()
        if s == "":
            return 0
        result = ""
        if s[0] in ('+', '-'):
            result += s[0]
            s = s[1:]

        for i in range(0, len(s)):
            if s[i].isnumeric():
                result += s[i]
            else:
                break

        if result == "":
            return 0

        try:
            result = int(result)
            if result > MAX_INT:
                return MAX_INT
            elif result < MIN_INT:
                return MIN_INT
            else:
                return result
        except:
            return 0


def main():
    sol = Solution()
    assert sol.atoi("42") == 42
    assert sol.atoi("4193 with words") == 4193
    assert sol.atoi("words and 987") == 0
    assert sol.atoi("-91283472332") == -2147483648


if __name__ == "__main__":
    main()