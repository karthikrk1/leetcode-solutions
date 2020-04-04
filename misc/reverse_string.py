"""
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
"""

class Solution:
    def reverse_string(self, s):
        """Modifying in place"""
        i = 0
        j = len(s) - 1
        while i <= j:
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
            i += 1
            j -= 1


def main():
    sol = Solution()
    case_1 = ["h","e","l","l","o"]
    case_2 = ["H","a","n","n","a","h"]
    sol.reverse_string(case_1)
    sol.reverse_string(case_2)
    assert case_1 == ["o","l","l","e","h"]
    assert case_2 == ["h","a","n","n","a","H"]


if __name__ == "__main__":
    main()