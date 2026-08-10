class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        s1=set()
        maxlength=0
        for right in range(len(s)):
            while s[right] in s1:
                s1.remove(s[left])
                left+=1
            s1.add(s[right])
            maxlength=max(maxlength,right-left+1)
        return maxlength        




        