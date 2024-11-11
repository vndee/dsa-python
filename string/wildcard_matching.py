class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(p), len(s)
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        dp[0][0] = True

        for i in range(1, m + 1):
            if p[i - 1] == "*":
                dp[i][0] = dp[i - 1][0]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[i - 1] == "*":
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                elif p[i - 1] == "?" or p[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]

        return dp[m][n]


if __name__ == "__main__":
    sol = Solution()
    # assert sol.isMatch("aa", "a") is False
    # assert sol.isMatch("aa", "*") is True
    # assert sol.isMatch("cb", "?a") is False
    assert sol.isMatch("abdc", "a*c") is True
    # assert sol.isMatch("acdcb", "a*c?b") is False
    # assert sol.isMatch("aab", "c*a*b") is False
    # assert sol.isMatch("adceb", "*a*b") is True
    # assert sol.isMatch("abcabczzzde", "*abc???de*") is True
    # assert sol.isMatch("c", "*?*") is True
    # assert sol.isMatch("b", "b*b") is False
    # assert sol.isMatch("b", "??") is False
    # assert sol.isMatch("adceb", "*a*b") is True
    # assert sol.isMatch("abcd", "abc*d") is True
