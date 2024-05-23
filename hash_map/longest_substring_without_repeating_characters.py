"""
Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters
Approach: Use a dictionary to store the index of the characters in the string. Traverse the string and keep track of the start of
the substring and the maximum length of the substring. If the character is already present in the dictionary and the start of the
substring is less than or equal to the index of the character, then update the start of the substring to the index of the character
plus one. Update the index of the character in the dictionary. Update the maximum length of the substring. Return the maximum length
of the substring.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        else:
            char_dict = {}
            max_len = 0
            start = 0
            for i in range(len(s)):
                if s[i] in char_dict:
                    start = max(start, char_dict[s[i]] + 1)
                char_dict[s[i]] = i
                max_len = max(max_len, i - start + 1)
            return max_len