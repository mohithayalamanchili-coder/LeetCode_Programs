class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        ans=len(nums)+1
        sum_=0
        for right in range(len(nums)):
            sum_+=nums[right]
            while sum_>=target:
                a=right-left+1
                ans=min(ans,a)
                sum_-=nums[left]
                left+=1 
        if ans==len(nums)+1:
            return 0       
        return ans          

        