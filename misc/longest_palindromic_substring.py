"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Input: "cbbd"
Output: "bb"
"""

class Solution:
    def lps(self, s):
        if not s or len(s) < 1:
            return ""
        start = 0
        end = 0
        for i in range(len(s)):
            len1 = self.expand(s, i, i)
            len2 = self.expand(s, i, i+1)
            maxlen = max(len1, len2)
            if maxlen > (end - start):
                start = i - ((maxlen-1)//2 )
                end = i + (maxlen // 2)
        return s[start:end+1]

    def expand(self, s, left, right):
        if not s or (left > right):
            return 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return (right - left - 1)


def main():
    sol = Solution()
    case_1 = sol.lps("babad")
    case_2 = sol.lps("cbbd")
    assert case_1 in ("aba", "bab")
    assert case_2 == "bb"

if __name__ == "__main__":
    main()
