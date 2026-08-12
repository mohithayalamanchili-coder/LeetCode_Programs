class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sum_=0
        result=[]
        for i in nums:
            sum_+=i
            result.append(sum_)
        return result    