#!/bin/python3
"""
Valid Anagram - https://leetcode.com/problems/valid-anagram/
Approach: Use a dictionary to store the frequency of characters in the first string. Traverse the second string and if the character
is not present in the dictionary or the frequency is 0, then return False. Otherwise, decrement the frequency of the character.
Time complexity: O(n)
Space complexity: O(n)
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        for c in s:
            d[c] = d.get(c, 0) + 1

        for c in t:
            if c not in d or d[c] == 0:
                return False

            d[c] -= 1

        return not any(d.values())