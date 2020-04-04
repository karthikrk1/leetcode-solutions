"""
Given an array of strings, group anagrams together.

Note:

All inputs will be in lowercase.
The order of your output does not matter.

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
"""

class Solution:
    def group_anagrams(self, strs):
        d = {}
        for st in strs:
            sorted_st = ''.join(sorted(st))
            if sorted_st in d:
                d[sorted_st].append(st)
            else:
                d[sorted_st] = [st]
        return d.values()


def main():
    assert Solution().group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [
        ["ate", "eat", "tea"],
        ["nat", "tan"],
        ["bat"]
    ]


if __name__ == '__main__':
    main()