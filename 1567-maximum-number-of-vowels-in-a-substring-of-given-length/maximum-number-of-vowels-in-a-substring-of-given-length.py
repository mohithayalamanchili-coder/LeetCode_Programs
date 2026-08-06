def is_v(ch):
    return ch in 'aeiou'

class Solution:

    
    
    def maxVowels(self, s: str, k: int) -> int:
        #compute the number of vowels in first
        #k-size substring
        first_window=s[:k]
        v_c=0
        for i in first_window:
            if is_v(i):
                v_c+=1
        mx=max(v_c,0)
        for i in range(k,len(s)):
            if is_v(s[i]):
                v_c+=1
            if is_v(s[i-k]):
                v_c-=1
            mx=max(mx,v_c)
        return mx                    