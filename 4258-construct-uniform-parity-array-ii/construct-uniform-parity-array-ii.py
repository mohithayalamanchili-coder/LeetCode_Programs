class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        mn=float('inf')
        for i in nums1:
            if i%2!=0:
                mn=min(mn,i)
        for i in nums1:
            if i%2==0 and mn!=float('inf') and i<mn:
                return False
        return True        


                

        