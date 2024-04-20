#!/bin/python3
"""
Find Right Interval - https://leetcode.com/problems/find-right-interval/
Approach: Sort the intervals based on the start time. For each interval, use binary search to find the right interval. Initialize
the answer array with -1. For each interval, find the left and right pointers. While the left pointer is less than the right pointer,
find the middle index. If the start time at the middle index is greater than the end time of the current interval, then update the
right pointer to the middle index. If the start time at the middle index is less than the end time of the current interval, then update
the left pointer to the middle index + 1. If the start time at the middle index is equal to the end time of the current interval, then
update the answer for the current interval to the middle index. If the left pointer is less than the length of the intervals and the
start time at the left pointer is greater than or equal to the end time of the current interval, then update the answer for the current
interval to the left pointer. Return the answer array.
Time complexity: O(n log n)
Space complexity: O(n)
"""

from typing import List


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        intervals = [(interval[0], interval[1], i) for i, interval in enumerate(intervals)]
        intervals.sort(key=lambda x: x[0])
        ans = [-1] * len(intervals)

        for i in range(len(intervals)):
            l, r = i, len(intervals)
            while l < r:
                m = (l + r) >> 1
                if intervals[m][0] > intervals[i][1]:
                    r = m
                elif intervals[m][0] < intervals[i][1]:
                    l = m + 1
                else:
                    ans[intervals[i][2]] = intervals[m][2]
                    break

            if l < len(intervals) and intervals[l][0] >= intervals[i][1]:
                ans[intervals[i][2]] = intervals[l][2]

        return ans