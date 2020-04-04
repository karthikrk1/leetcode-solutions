"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
"""

class Solution:
    def isValid(self, s):
        d = {')': '(', '}':'{', ']':'['}
        stack = []
        for i in s:
            if i in d.values():
                stack.append(i)
            else:
                try:
                    if stack[-1] == d[i]:
                        stack.pop()
                    else:
                        return False
                except:
                    return False
        return stack == []


def main():
    sol = Solution()
    assert sol.isValid("()")
    assert sol.isValid("()[]{}")
    assert not sol.isValid("(]")
    assert not sol.isValid("([)]")
    assert sol.isValid("{[]}")


if __name__ == '__main__':
    main()