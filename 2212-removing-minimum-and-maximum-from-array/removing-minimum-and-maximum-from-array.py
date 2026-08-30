class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n=len(nums)
        min_index=nums.index(min(nums))
        max_index=nums.index(max(nums))
        if min_index>max_index:
            min_index,max_index=max_index,min_index
        front=max_index+1
        back=n-min_index
        both=(min_index+1)+(n-max_index)
        return min(front,back,both)


        