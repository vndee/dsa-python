#!/bin/python3
"""
Bubble Sort - https://www.hackerrank.com/challenges/ctci-bubble-sort
Approach: Bubble sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements
and swaps them if they are in the wrong order.
Time complexity: O(n^2)
Space complexity: O(1)
"""

def countSwaps(a):
    ans = 0
    for i in range(0, len(a) - 1):
        for j in range(i, len(a)):
            if a[i] > a[j]:
                ans = ans + 1
                a[i], a[j] = a[j], a[i]

    print(f"Array is sorted in {ans} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")


if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
