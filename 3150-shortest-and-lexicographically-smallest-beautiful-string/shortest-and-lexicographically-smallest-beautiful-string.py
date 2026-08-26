class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        pos=[]
        for i in range(len(s)):
            if s[i]=='1':
                pos.append(i)
        ans=""
        for i in range(len(pos) - k + 1):
            start = pos[i]
            end = pos[i + k - 1]

            sub = s[start:end + 1]
            if ans=="":
                ans=sub
            elif len(sub)<len(ans):
                ans=sub
            elif len(sub)==len(ans) and sub<ans:
                ans=sub
        return ans        


        