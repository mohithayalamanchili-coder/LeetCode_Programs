import heapq
from collections import defaultdict
class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:

        n = len(nums)

        low = []       # Max heap (negative values)
        high = []      # Min heap
        delayed = defaultdict(int)

        low_size = high_size = 0
        low_sum = high_sum = 0

        def prune(heap, sign):
            while heap:
                v = sign * heap[0]
                if delayed[v] == 0:
                    break
                heapq.heappop(heap)
                delayed[v] -= 1

        def rebalance():
            nonlocal low_size, high_size
            nonlocal low_sum, high_sum

            if low_size > high_size + 1:
                v = -heapq.heappop(low)
                low_size -= 1
                low_sum -= v
                heapq.heappush(high, v)
                high_size += 1
                high_sum += v
                prune(low, -1)

            elif low_size < high_size:
                v = heapq.heappop(high)
                high_size -= 1
                high_sum -= v
                heapq.heappush(low, -v)
                low_size += 1
                low_sum += v
                prune(high, 1)

        def add(v):
            nonlocal low_size, high_size
            nonlocal low_sum, high_sum

            prune(low, -1)

            if not low or v <= -low[0]:
                heapq.heappush(low, -v)
                low_size += 1
                low_sum += v
            else:
                heapq.heappush(high, v)
                high_size += 1
                high_sum += v

            rebalance()

        def remove(v):
            nonlocal low_size, high_size
            nonlocal low_sum, high_sum

            prune(low, -1)
            prune(high, 1)

            delayed[v] += 1

            if v <= -low[0]:
                low_size -= 1
                low_sum -= v

                if v == -low[0]:
                    prune(low, -1)
            else:
                high_size -= 1
                high_sum -= v

                if high and v == high[0]:
                    prune(high, 1)

            rebalance()

        def get_cost():
            median = -low[0]

            return (median * low_size - low_sum +
                    high_sum - median * high_size)

        costs = []

        for i in range(n):
            add(nums[i])

            if i >= x:
                remove(nums[i - x])

            if i >= x - 1:
                costs.append(get_cost())

        # DP
        INF = float('inf')
        prev = [0] * (n + 1)

        for j in range(1, k + 1):
            curr = [INF] * (n + 1)

            for i in range(1, n + 1):
                curr[i] = curr[i - 1]

                if i >= x:
                    curr[i] = min(
                        curr[i],
                        prev[i - x] + costs[i - x]
                    )

            prev = curr

        return prev[n]