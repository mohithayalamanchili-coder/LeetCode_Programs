class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left=0
        currentWhite=0
        lst=list(blocks)
        min_count=float('inf')
        for right in range(len(lst)):
            if lst[right]=='W':
                currentWhite+=1
            if right>=k-1:
                min_count=min(min_count,currentWhite)
                
                if lst[left]=='W':
                    currentWhite-=1
                    
                left+=1
        return min_count           
                


        