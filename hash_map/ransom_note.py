"""
Ransom Note - https://leetcode.com/problems/ransom-note/
Approach: Use a dictionary to store the frequency of characters in the magazine. Traverse the ransom note and if the character
is not present in the dictionary or the frequency is 0, then return False. Otherwise, decrement the frequency of the character.
Time complexity: O(n)
Space complexity: O(n)
"""


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = {}
        for c in magazine:
            d[c] = d.get(c, 0) + 1

        for c in ransomNote:
            if c not in d or d[c] == 0:
                return False

            d[c] -= 1

        return True
