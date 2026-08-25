class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        a=nums
        i=1
        while True:
            if k*i in a:
                i+=1
            else:
                return k*i    

   
            

        