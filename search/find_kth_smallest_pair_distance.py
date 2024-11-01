class Solution(object):
    def _smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n_max = max(nums)
        freq = [0] * (n_max + 1)

        for x in nums:
            freq[x] = freq[x] + 1

        for i in range(1, n_max + 1):
            freq[i] = freq[i - 1] + freq[i]

        comb = lambda x: (x * (x - 1)) // 2

        l, r = 0, n_max
        while l < r:
            m = (l + r) >> 1

            cnt = 0
            for i in range(m, n_max + 1, 1):
                x = comb(freq[i] - freq[i - m - 1]) if i - m > 0 else comb(freq[i])
                if m > 1 and i >= m + 1:
                    x -= comb(freq[i - 1] - freq[i - m - 1]) if i - m > 0 else comb(freq[i - 1])

                cnt = cnt + x

                if cnt > k:
                    break

            if cnt >= k:
                r = m
            else:
                l = m + 1

        return r

    def smallestDistancePair(self, nums, k):
        nums.sort()
        n = len(nums)

        l, r = 0, nums[-1] - nums[0]

        while l < r:
            m = (l + r) // 2
            cnt = 0
            j = 0

            for i in range(n):
                while j < n and nums[j] - nums[i] <= m:
                    j += 1
                cnt += j - i - 1

            if cnt >= k:
                r = m
            else:
                l = m + 1

        return r

    def test(self, nums, k):
        s = []
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                s.append(abs(nums[i] - nums[j]))

        s = sorted(s)
        return s[k - 1]


if __name__ == "__main__":
    sol = Solution()
    # print(sol.smallestDistancePair([1, 3, 1], 1))
    # print(sol.smallestDistancePair([1, 6, 1], 2))
    # a = [38, 33, 57, 65, 13, 2, 86, 75, 4, 56]
    # a = [1, 1, 3, 4, 4, 7, 0, 9, 2]
    a = [1, 2, 3, 4, 5, 6]
    print(sol.smallestDistancePair(a, 10))
    print(sol.test(a, 10))