#!/bin/python3
"""
Word Pattern - https://leetcode.com/problems/word-pattern/
Approach: Use two dictionaries to store the mapping of characters from the pattern to the words and vice versa. Traverse the pattern
and words and if the mapping is not present, then add the mapping to the dictionaries. If the mapping is present, then check if the
mapping is the same as the current word. If not, then return False.
Time complexity: O(n)
Space complexity: O(n)
"""


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(" ")
        d1, d2 = {}, {}

        if len(s) != len(pattern):
            return False

        for i in range(len(pattern)):
            if pattern[i] not in d1:
                d1[pattern[i]] = s[i]
            elif d1[pattern[i]] != s[i]:
                return False

            if s[i] not in d2:
                d2[s[i]] = pattern[i]
            elif d2[s[i]] != pattern[i]:
                return False

        return True
