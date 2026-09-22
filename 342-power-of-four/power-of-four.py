class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        i=0
        while pow(4,i)<=n:
            if n==pow(4,i):
                return True
            i+=1    
        return False           
        