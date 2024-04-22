"""
Snapshot Array - https://leetcode.com/problems/snapshot-array/
Approach: Use a dictionary to store the values of the array. When a snapshot is taken, store the snapshot id and the value of
the array at that point in time. To get the value of the array at a given index and snapshot id, use binary search to find the
value with the largest snapshot id less than or equal to the given snapshot id. If the snapshot id is less than the smallest
snapshot id for the index, then return 0.
Time complexity: O(log n) for set and get operations
Space complexity: O(n)
"""


class SnapshotArray:
    def __init__(self, length: int):
        self.d = {}
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        if index not in self.d:
            self.d[index] = []

        while self.d[index] and self.d[index][-1][0] == self.snap_id:
            self.d[index].pop()

        self.d[index].append((self.snap_id, val))

    def snap(self) -> int:
        snap_id = self.snap_id
        self.snap_id = self.snap_id + 1
        return snap_id

    def get(self, index: int, snap_id: int) -> int:
        if index not in self.d:
            return 0

        values = self.d[index]
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) >> 1
            if values[m][0] > snap_id:
                r = m - 1
            elif values[m][0] < snap_id:
                l = m + 1
            else:
                return values[m][1]

        if r >= 0 and values[r][0] <= snap_id:
            return values[r][1]

        return 0
