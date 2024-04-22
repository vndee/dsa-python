"""
Search in Rotated Sorted Array - https://leetcode.com/problems/search-in-rotated-sorted-array/
Approach: Use binary search to find the pivot element. If the pivot element is not found, then the array is not rotated. If the
target element is less than or equal to the last element of the array, then the target element is in the right half of the array.
Otherwise, the target element is in the left half of the array. Use binary search to find the target element in the left or right
half of the array.
Time complexity: O(log n)
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 1:
            return 0 if nums[0] == target else -1

        l, r = 0, n - 1
        while l < r:
            m = (l + r) >> 1
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        pivot = l
        l, r = 0, n - 1
        while l <= r:
            m = (l + r) >> 1
            mid = (m + pivot) % n
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                l = m + 1
            else:
                r = m - 1

        return -1
