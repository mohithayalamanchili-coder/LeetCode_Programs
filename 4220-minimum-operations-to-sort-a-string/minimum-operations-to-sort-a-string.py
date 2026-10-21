class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
       
        if s == ''.join(sorted(s)):
            return 0
        if n == 2:
            return -1
            
        first = s[0]
        last = s[-1]
        mn = min(s)
        mx = max(s)
        if first == mn or last == mx:
            return 1
         
        if first == mx and last == mn and s.count(mx) == 1 and s.count(mn) == 1:
            return 3
     
        return 2
        