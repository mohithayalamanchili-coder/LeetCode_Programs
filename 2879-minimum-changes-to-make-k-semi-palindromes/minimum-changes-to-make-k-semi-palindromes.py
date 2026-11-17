class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        cost = [[0] * (n + 1) for _ in range(n)]

        for l in range(n):
            for r in range(l + 2, n + 1):
                length = r - l
                best = float('inf')

                for d in range(1, length):
                    if length % d == 0:
                        changes = 0

                        for i in range(d):
                            left = i
                            right = length - d + i

                            while left < right:
                                if s[l + left] != s[l + right]:
                                    changes += 1

                                left += d
                                right -= d

                        best = min(best, changes)

                cost[l][r] = best

        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for j in range(1, k + 1):
            for i in range(2 * j, n + 1):
                for p in range(2 * (j - 1), i - 1):
                    dp[i][j] = min(
                        dp[i][j],
                        dp[p][j - 1] + cost[p][i]
                    )

        return dp[n][k]
