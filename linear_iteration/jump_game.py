"""
Jump Game - https://leetcode.com/problems/jump-game/
Approach: Traverse the array from right to left and keep track of the minimum index that can reach the end. If the current
index can reach the minimum index, then update the minimum index to the current index. If the minimum index is 0, then return
True, else return False.
Time complexity: O(n)
Space complexity: O(1)
"""
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reachable = 0
        n = len(nums)

        if n == 1:
            return True

        for i in range(n):
            if i > max_reachable:
                return False

            max_reachable = max(max_reachable, i + nums[i])
            if max_reachable >= n - 1:
                return True

        return False
