class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        left=0
        lst=list(s)
        vow_count=0
        count=0
        for right in range(len(lst)):
            if lst[right] in 'aeiou':
                count+=1
            if right>=k:
                if s[left] in 'aeiou':
                    count-=1
                left+=1 
            if right>=k-1:
                vow_count=max(vow_count,count)      
            
            

                
                
        return vow_count    
                
        