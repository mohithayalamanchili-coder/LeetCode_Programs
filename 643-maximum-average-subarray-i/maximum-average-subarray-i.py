class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        #sliding window (Fixed-length sliding window)
        # Brute force solution - fails due to len(n) can be as long as 10^5
        # Generate all sub-arrays and keep the average of those whose length is k
        maxAvg=-1000000000
        left=0
        currentSum=0
        for right in range(len(nums)):
            currentSum+=nums[right]
            if right>=k-1:
                avg=currentSum/k
                maxAvg=max(maxAvg,avg)
                #Subtracting the value on left (window size is exceed k)
                currentSum-=nums[left]
                left+=1
        return maxAvg        