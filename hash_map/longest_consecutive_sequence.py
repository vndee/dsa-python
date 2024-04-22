"""
Longest Consecutive Sequence - https://leetcode.com/problems/longest-consecutive-sequence/
Approach: Use a set to store the elements of the array. Traverse the array and for each element, check if the element - 1 is not
present in the set. If it is not present, then it is the start of a sequence. Increment the element by 1 and check if the element
is present in the set. If it is present, then increment the length of the sequence. Update the maximum length of the sequence.
Time complexity: O(n)
Space complexity: O(n)
"""

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        max_length = 0

        for num in nums:
            if num - 1 not in s:
                length = 1
                current = num

                while current + 1 in s:
                    length += 1
                    current += 1

                max_length = max(max_length, length)

        return max_length
