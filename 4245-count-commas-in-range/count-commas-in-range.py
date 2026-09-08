class Solution:
    def countCommas(self, n: int) -> int:
        c=0
        for i in range(n+1):
            if i>=1000:
                c+=1
            elif i>10000:
                c+=1
            elif i>100000:
                c+=1
        return c                


         