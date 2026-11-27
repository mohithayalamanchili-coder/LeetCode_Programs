class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        minPrice = min(p for f, p in items)

        dp = [0] * (budget + 1)

        for i in range(n):
            f, p = items[i]

            free = 0
            for j in range(n):
                if i != j and items[j][0] % f == 0:
                    free += 1

            value = 1 + free

            for b in range(budget, p - 1, -1):
                dp[b] = max(dp[b], dp[b-p] + value)

        ans = 0

        for b in range(budget + 1):
            ans = max(ans, dp[b] + (budget-b) // minPrice)

        return ans