class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        ans = [0] * k
        dp = [0] * k
        for num in nums:
            new = [0] * k
            r = num % k
            new[r] += 1
            for old_r in range(k):
                new[(old_r * r) % k] += dp[old_r]
            for r in range(k):
                ans[r] += new[r]
            dp = new
        return ans