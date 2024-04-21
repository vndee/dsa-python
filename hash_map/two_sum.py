#!/bin/python3
"""
Two Sum - https://leetcode.com/problems/two-sum/
Approach: Use a dictionary to store the index of the elements. Traverse the array and if the difference between the target
and the current element is in the dictionary, then return the indices of the elements.
Time complexity: O(n)
Space complexity: O(n)
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, e in enumerate(nums):
            if target - e in d:
                return [d[target - e], i]

            d[e] = i
