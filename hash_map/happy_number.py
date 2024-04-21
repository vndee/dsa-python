#!/bin/python3
"""
Happy Number - https://leetcode.com/problems/happy-number/
Approach: Use a set to store the sum of the squares of the digits of the number. If the sum is 1, then return True. If the sum is
already present in the set, then return False. Otherwise, add the sum to the set and continue the process.
Time complexity: O(log n)
Space complexity: O(log n)
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        seen = {}
        while n != 1 and n not in seen:
            seen[n] = 1
            n = sum(int(digit) ** 2 for digit in str(n))

        return n == 1
