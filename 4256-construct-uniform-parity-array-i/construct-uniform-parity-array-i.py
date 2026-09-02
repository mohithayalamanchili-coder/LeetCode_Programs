class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        nums2=[]
        for i in range(len(nums1)):
            for j in range(len(nums1)):
                if j!=i:
                    a=nums1[i]-nums1[j]
                    if a%2!=0:
                        nums2.append(a)
        for i in range(len(nums2)):
            if nums2[i] % 2 != nums2[0] % 2:
                return False

        return True                

        