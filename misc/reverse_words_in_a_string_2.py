"""
Given an input string , reverse the string word by word.


Note:

A word is defined as a sequence of non-space characters.
The input string does not contain leading or trailing spaces.
The words are always separated by a single space.
Follow up: Could you do it in-place without allocating extra space?

Input:  ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
"""

class Solution:
    def rev_words(self, s):
        """Modify in place"""
        sentence = "".join(s)
        reverse_sent = " ".join(sentence.split(" ")[::-1])
        for i in range(len(reverse_sent)):
            s[i] = reverse_sent[i]


def main():
    case_1 = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
    Solution().rev_words(case_1)
    assert case_1 == ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]


if __name__ == '__main__':
    main()