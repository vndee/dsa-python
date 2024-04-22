"""
Find First and Last Position of Element in Sorted Array - https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
Approach: Use binary search to find the leftmost and rightmost indices of the target element. Initialize the left and right pointers
to 0 and n - 1 respectively. While the left pointer is less than or equal to the right pointer, find the middle index. If the
element at the middle index is less than the target, then update the left pointer to the middle index + 1. If the element at the
middle index is greater than the target, then update the right pointer to the middle index - 1. If the element at the middle index
is equal to the target, then update the right pointer to the middle index - 1. If the left pointer is less than n and the element
at the left pointer is equal to the target, then update the leftmost index to the left pointer. If the right pointer is greater
than or equal to 0 and the element at the right pointer is equal to the target, then update the rightmost index to the right pointer.
Return the leftmost and rightmost indices.
Time complexity: O(log n)
Space complexity: O(1)
"""

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        L, R = -1, -1
        n = len(nums)

        l, r = 0, n - 1
        while l <= r:
            m = (l + r) >> 1
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                r = m - 1

        if l < n and nums[l] == target:
            L = l

        l, r = 0, n - 1
        while l <= r:
            m = (l + r) >> 1
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1

        if r >= 0 and nums[r] == target:
            R = r

        return [L, R]
