"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Input: "A man, a plan, a canal: Panama"
Output: true

Input: "race a car"
Output: false
"""

class Solution:
    def isPalindrome(self, s):
        if s == "":
            return True
        clean_str = "".join([st for st in s.lower() if st.isalnum()])
        return clean_str == clean_str[::-1]


def main():
    sol = Solution()
    assert sol.isPalindrome("A man, a plan, a canal: Panama")
    assert not sol.isPalindrome("race a car")


if __name__ == "__main__":
    main()