class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result_set=set()
        
        nums.sort()
        for i in range(len(nums)):
            left=i+1
            right=len(nums)-1
            while left<right:
                t_sum=nums[i]+nums[left]+nums[right]
                triplet=nums[i],nums[left],nums[right]
                if t_sum==0:
                    result_set.add(tuple(triplet))
                    left+=1
                    right-=1
                elif t_sum>0:
                    right-=1
                else: 
                    left+=1
        return list(result_set)            


        

