"""
Two Sum II - Input array is sorted - https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
Approach: Use a dictionary to store the index of the elements. Traverse the array and if the difference between the target
and the current element is in the dictionary, then return the indices of the elements.
Time complexity: O(n)
Space complexity: O(n)
"""

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}
        for i, e in enumerate(numbers):
            if target - e in d:
                return [d[target - e] + 1, i + 1]

            d[e] = i
