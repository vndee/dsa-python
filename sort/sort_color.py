#!/bin/python3
"""
Sort Colors - https://leetcode.com/problems/sort-colors/
Approach: Bubble sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements
and swaps them if they are in the wrong order.
Time complexity: O(n^2)
Space complexity: O(1)
"""

from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(0, len(nums) - 1):
            for j in range(i, len(nums)):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]

        return nums
