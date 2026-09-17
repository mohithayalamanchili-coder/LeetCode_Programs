class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        INF = 10**9
        best = [INF] * n
        left = 0
        curr = 0
        ans = INF
        for right in range(n):
            curr += arr[right]
            while curr > target:
                curr -= arr[left]
                left += 1
            if curr == target:
                length = right - left + 1
                if left > 0:
                    ans = min(ans, length + best[left - 1])
                best[right] = length
            if right > 0:
                best[right] = min(best[right], best[right - 1])
        return -1 if ans == INF else ans
        