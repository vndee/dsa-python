"""
Merge Intervals - https://leetcode.com/problems/merge-intervals/
Approach: Sort the intervals based on the start time. Initialize the result with the first interval. Iterate through the
intervals and if the start time of the current interval is less than or equal to the end time of the last interval in the
result, then update the end time of the last interval to the maximum of the end time of the last interval and the end time
of the current interval. Otherwise, add the current interval to the result. Return the result.
Time complexity: O(nlogn)
Space complexity: O(n)
"""

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort(key=lambda x: x[0])

        res.append(intervals[0])
        for i in range(1, len(intervals)):
            if intervals[i][0] <= res[-1][1] and intervals[i][1] <= res[-1][1]:
                continue
            if intervals[i][0] <= res[-1][1]:
                res[-1][1] = intervals[i][1]
            else:
                res.append(intervals[i])

        return res
