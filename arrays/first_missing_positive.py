class Solution(object):
    def _firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 1 if nums[0] < 1 else 1 if nums[0] > 1 else 2

        nums = sorted(nums)
        min_pos = 0

        while min_pos < len(nums) and nums[min_pos] <= 0:
            min_pos = min_pos + 1

        if min_pos == len(nums):
            return 1

        if nums[min_pos] > 1:
            return 1

        for i in range(min_pos + 1, len(nums), 1):
            if nums[i] - nums[i - 1] > 1:
                return nums[i - 1] + 1

        return nums[-1] + 1

    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(0, len(nums)):
            if nums[i] <= 0 or nums[i] > len(nums):
                nums[i] = len(nums) + 2

        for i in range(len(nums)):
            x = abs(nums[i])

            if x <= len(nums):
                nums[x - 1] = -1 * abs(nums[x - 1])

        for i in range(len(nums)):
            if nums[i] >= 0:
                return i + 1

        return len(nums) + 1


if __name__ == "__main__":
    sol = Solution()
    # print(sol.firstMissingPositive([-1, -2]))
    # print(sol.firstMissingPositive([3]))
    # print(sol.firstMissingPositive([1]))
    print(sol.firstMissingPositive([-5]))
    # print(sol.firstMissingPositive([0]))
    # print(sol.firstMissingPositive([5, 1, 3, 2]))
    # print(sol.firstMissingPositive([1, 2, 0]))
    # print(sol.firstMissingPositive([3, 4, -1, 1]))
    # print(sol.firstMissingPositive([7, 8, 9, 11, 12]))
