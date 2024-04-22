"""
Time Based Key-Value Store - https://leetcode.com/problems/time-based-key-value-store/
Approach: Use a dictionary to store the key and the list of values. For each key, store the timestamp and the value. To get the
value for a key at a given timestamp, use binary search to find the value with the largest timestamp less than or equal to the given
timestamp. If the timestamp is less than the smallest timestamp for the key, then return an empty string.
Time complexity: O(log n) for set and get operations
Space complexity: O(n)
"""


class TimeMap:
    def __init__(self):
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.d:
            self.d[key] = []
        self.d[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ""

        values = self.d[key]
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) >> 1
            if values[m][0] > timestamp:
                r = m - 1
            elif values[m][0] < timestamp:
                l = m + 1
            else:
                return values[m][1]

        if r >= 0 and values[r][0] <= timestamp:
            return values[r][1]

        return ""
