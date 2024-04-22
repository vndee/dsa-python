"""
Contains Duplicate II - https://leetcode.com/problems/contains-duplicate-ii/
Approach: Use a dictionary to store the index of the elements. Traverse the array and if the difference between the current index
and the index of the element is less than or equal to k, then return True. Otherwise, update the index of the element in the dictionary.
Time complexity: O(n)
Space complexity: O(n)
"""

from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for i, e in enumerate(nums):
            if e in d and i - d[e] <= k:
                return True

            d[e] = i

        return False
