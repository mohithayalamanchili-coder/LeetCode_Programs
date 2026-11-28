class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)

        freq = [0] * (n + 1)

        for f, p in items:
            freq[f] += 1

        cnt = [0] * (n + 1)

        for i in range(1, n + 1):
            for j in range(i, n + 1, i):
                cnt[i] += freq[j]

        arr = []
        min_price = min(p for f, p in items)

        for f, p in items:
            c = cnt[f] - 1
            if c > 0 and p < 2 * min_price:
                arr.append((p, c))

        arr.sort()

        caps = [0]
        costs = [0]

        for p, c in arr:
            caps.append(caps[-1] + c)
            costs.append(costs[-1] + p * c)

        def check(k):
            q = min(k // 2, caps[-1])

            lo, hi = 0, len(arr)

            while lo < hi:
                mid = (lo + hi + 1) // 2
                if caps[mid] <= q:
                    lo = mid
                else:
                    hi = mid - 1

            cost = costs[lo]

            if lo < len(arr):
                cost += (q - caps[lo]) * arr[lo][0]

            cost += (k - 2 * q) * min_price

            return cost <= budget

        lo, hi = 0, 2 * (budget // min_price) + 1

        while lo + 1 < hi:
            mid = (lo + hi) // 2

            if check(mid):
                lo = mid
            else:
                hi = mid

        return lo
