class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        total=sum(nums)
        target=total-x
        if target<0:
            return -1
        if target==0:
            return len(nums)
        sum_=0
        left=0
        mx=-1
        for right in range(len(nums)):
            sum_+=nums[right]
            while sum_>target:
                sum_-=nums[left]
                left+=1 
            if sum_==target:
                mx=max(right-left+1,mx)
        if mx==-1:
            return -1        
        return len(nums)-mx           
        