class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        temp=word
        c=0
        while temp in sequence:
            c+=1
            temp+=word
        return c    
