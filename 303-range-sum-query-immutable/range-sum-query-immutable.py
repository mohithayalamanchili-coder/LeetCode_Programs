class NumArray:

    def __init__(self, nums: List[int]):
        self.nums=nums
        #self.nums=list(itertools.accumulate(self.nums),intial=0)
        self.prefix=[0]
        rs=0
        for i in self.nums:
            rs+=i
            self.prefix.append(rs)
        

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right+1]-self.prefix[left]
        #return sum(self.nums[left:right+1])
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)