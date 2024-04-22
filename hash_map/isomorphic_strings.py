"""
Isomorphic Strings - https://leetcode.com/problems/isomorphic-strings/
Approach: Use two dictionaries to store the mapping of characters from string s to string t and vice versa. Traverse the strings
and if the mapping is not present, then add the mapping to the dictionaries. If the mapping is present, then check if the mapping
is the same as the current character. If not, then return False.
Time complexity: O(n)
Space complexity: O(n)
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d1, d2 = {}, {}
        for i in range(len(s)):
            if s[i] not in d1:
                d1[s[i]] = t[i]
            elif d1[s[i]] != t[i]:
                return False

            if t[i] not in d2:
                d2[t[i]] = s[i]
            elif d2[t[i]] != s[i]:
                return False

        return True
