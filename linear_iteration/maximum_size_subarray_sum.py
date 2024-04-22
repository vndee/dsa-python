"""
Minimum Size Subarray Sum - https://leetcode.com/problems/minimum-size-subarray-sum
Approach: Use two pointers to keep track of the left and right indices of the subarray. Initialize the left and right pointers
to 0 and 1 respectively. Initialize the sliding sum to the sum of the first two elements. If the sliding sum is greater than
or equal to the target, then update the answer to the length of the subarray. While the right pointer is less than the length
of the array, keep adding the element at the right pointer to the sliding sum. If the sliding sum is greater than or equal to
the target, then update the answer to the length of the subarray. While the sliding sum is greater than or equal to the target,
keep subtracting the element at the left pointer from the sliding sum. If the sliding sum is greater than or equal to the
target, then update the answer to the length of the subarray. Return the answer.
Time complexity: O(n)
Space complexity: O(1)
"""

from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0 if nums[0] < target else 1

        if nums[0] > target:
            return 1

        l, r, sliding_sum = 0, 2, nums[0] + nums[1]
        ans = 2 if sliding_sum >= target else -1
        while l < len(nums) and r < len(nums):
            while sliding_sum < target and r < len(nums):
                sliding_sum = sliding_sum + nums[r]
                r = r + 1
                if sliding_sum >= target:
                    ans = r - l if ans == -1 else min(ans, r - l)
            while sliding_sum >= target:
                sliding_sum = sliding_sum - nums[l]
                l = l + 1
                if sliding_sum >= target:
                    ans = r - l if ans == -1 else min(ans, r - l)

        return max(ans, 0)
