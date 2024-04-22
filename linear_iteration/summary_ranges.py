"""
Summary Ranges - https://leetcode.com/problems/summary-ranges/
Approach: Iterate through the array and keep track of the start and end of the range. If the next element is not equal to the
current element plus 1, then add the range to the result. If the range has only one element, then add only the start element.
Time complexity: O(n)
Space complexity: O(1)
"""

from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        start, end = nums[0], nums[0]
        res = []

        for i in range(1, len(nums)):
            if nums[i] == end + 1:
                end = nums[i]
            else:
                if start == end:
                    res.append(str(start))
                else:
                    res.append(f"{start}->{end}")
                start, end = nums[i], nums[i]

        if start == end:
            res.append(str(start))
        else:
            res.append(f"{start}->{end}")

        return res
