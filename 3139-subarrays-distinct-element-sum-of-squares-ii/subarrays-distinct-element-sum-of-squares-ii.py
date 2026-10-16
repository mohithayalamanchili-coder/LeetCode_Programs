class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        sum1 = [0] * (4 * n)
        sum2 = [0] * (4 * n)
        lazy = [0] * (4 * n)
        def push(node, l, r):
            if lazy[node] == 0:
                return
            v = lazy[node]
            left = node * 2
            right = left + 1
            mid = (l + r) // 2
            for child, length in ((left, mid - l + 1),
                                  (right, r - mid)):
                old = sum1[child]
                sum2[child] = (sum2[child] + 2 * v * old
                               + v * v * length) % MOD
                sum1[child] = (sum1[child] + v * length) % MOD
                lazy[child] += v

            lazy[node] = 0
        def update(node, l, r, ql, qr):
            if ql <= l and r <= qr:
                length = r - l + 1
                v = 1
                sum2[node] = (sum2[node] + 2 * sum1[node]
                              + length) % MOD
                sum1[node] = (sum1[node] + length) % MOD
                lazy[node] += v
                return
            push(node, l, r)
            mid = (l + r) // 2
            if ql <= mid:
                update(node * 2, l, mid, ql, qr)
            if qr > mid:
                update(node * 2 + 1, mid + 1, r, ql, qr)
            sum1[node] = (sum1[node * 2] + sum1[node * 2 + 1]) % MOD
            sum2[node] = (sum2[node * 2] + sum2[node * 2 + 1]) % MOD
        last = {}
        ans = 0
        for i, x in enumerate(nums):
            p = last.get(x, -1)
            update(1, 0, n - 1, p + 1, i)
            last[x] = i
            ans = (ans + sum2[1]) % MOD
        return ans       