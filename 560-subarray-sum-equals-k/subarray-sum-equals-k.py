class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Prefix + Hashmap Solution
        csum=0 # this is our prefix sum
        subcount=0 # how many subarrays have we seen with sum k
        seen={0:1} # hashmap to store prefix sum found so far
        for i in nums:
            # compute prefix_sum
            csum+=i
            # required prefix_sum ( prefix(l-1),history)
            req=csum-k
            # check if req in seen prefixes so far
            if req in seen:
                subcount+=seen[req] # add thr number of times we seen that prefixes
            # push the current prefix in hashmap
            seen[csum]=seen.get(csum,0)+1
        return subcount        
        