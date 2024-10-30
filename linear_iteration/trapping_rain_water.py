class Solution(object):
    def trap_1(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        # Time: O(N)
        # Space: O(N)
        ans, j = 0, height[0]
        l_max, r_max = [0] * len(height), [0] * len(height)

        for i in range(len(height)):
            l_max[i] = j
            j = max(j, height[i])

        j = height[-1]
        for i in range(len(height) - 1, -1, -1):
            r_max[i] = j
            j = max(j, height[i])

        for i in range(1, len(height) - 1):
            h = min(l_max[i], r_max[i]) - height[i]
            ans += h if h > 0 else 0

        return ans

    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        # Time: O(N)
        # Space: O(1)
        if not height:
            return 0

        left, right = 0, len(height) - 1
        left_max = right_max = ans = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    ans += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    ans += right_max - height[right]
                right -= 1

        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    print(sol.trap([4, 2, 0, 3, 2, 5]))
