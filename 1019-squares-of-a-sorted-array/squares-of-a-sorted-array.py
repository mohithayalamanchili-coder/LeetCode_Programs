class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        x=[]
        for i in range(len(nums)):
            a=nums[i]*nums[i]
            x.append(a)
            x.sort()

        return x 