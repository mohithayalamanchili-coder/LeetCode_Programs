class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        max_count=0
        for ch in nums:
            if ch==1:
                count+=1
            else:
                max_count=max(max_count,count) 
                count=0
        return max(max_count,count)                              
                
                
        