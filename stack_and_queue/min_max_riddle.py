#!/bin/python3
"""
Min Max Riddle - https://www.hackerrank.com/challenges/min-max-riddle
Approach: Use a stack to store the indices of the array elements. For each element, find the length of the window that
contains the element as the minimum element. The maximum value of the window length is the answer.
Time complexity: O(n)
Space complexity: O(n)
"""

import os


def riddle(arr):
    arr.append(-1)
    n = arr.__len__()
    res = [0] * (n - 1)
    st = []

    i = 0
    while i < n:
        if not st or arr[i] > arr[st[-1]]:
            st.append(i)
            i += 1
        else:
            val = arr[st.pop()]
            if st:
                len = i - st[-1] - 1
            else:
                len = i
            res[len - 1] = max(val, res[len - 1])

    for i in range(n - 3, -1, -1):
        res[i] = max(res[i], res[i + 1])

    return res


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = riddle(arr)

    fptr.write(" ".join(map(str, res)))
    fptr.write("\n")

    fptr.close()
