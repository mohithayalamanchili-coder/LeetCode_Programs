class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        left=0
        sm=0
        c=0
        for right in range(len(arr)):
            sm+=arr[right]
            if right>=k-1:
                avg=sm/k
                if avg>=threshold:
                    c+=1
                sm-=arr[left]
                left+=1
        return c            
        