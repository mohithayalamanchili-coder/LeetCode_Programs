class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftsum=0
        rightsum=0
        
        prefixsum=list(itertools.accumulate(nums,initial=0))
        for i in range(len(nums)):
            leftsum=prefixsum[i]
            rightsum=prefixsum[len(nums)]-prefixsum[i+1]
            if leftsum==rightsum:
                return i
        return -1        