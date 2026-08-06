class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        left=0
        sum_=0
        count=0
        for right in range(len(arr)):
            
            sum_+=arr[right]
            if right>=k-1:

                avg=sum_/k
                if avg>=threshold:
                    count+=1
                sum_-=arr[left]    
                left+=1    
                
                
        return count      
                   
        

        