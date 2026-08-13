class Solution:
    def characterReplacement(self, s, k):
        left = 0
        max_count = 0
        max_length = 0
        freq = {}

        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1
            max_count = max(max_count, freq[s[right]])

            while (right - left + 1) - max_count > k:
                freq[s[left]] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length