"""
Find Minimum in Rotated Sorted Array - https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
Approach: Use binary search to find the pivot element. If the pivot element is not found, then the array is not rotated. The minimum
element is the element at the pivot index. If the pivot element is found, then the minimum element is the element at the next index.
Time complexity: O(log n)
Space complexity: O(1)
"""

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) >> 1
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        return nums[l]
