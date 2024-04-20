#!/bin/python3
"""
Remove Duplicates from Sorted Array II - https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
Approach: Use three pointers to keep track of the current element, the next element and the position to insert the next
element. If the next element is equal to the current element and the current element is equal to the previous element,
then set the next element to 0. Otherwise, set the next element to the position to insert the next element and update the
current and next pointers.
Time complexity: O(n)
Space complexity: O(1)
"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j, k = 1, 2, 2
        while i < len(nums) and j < len(nums):
            if nums[j] == nums[i] and nums[i] == nums[i - 1]:
                nums[j] = 0
                j = j + 1
            else:
                nums[k] = nums[j]
                i = k
                j = j + 1
                k = k + 1

        return k
