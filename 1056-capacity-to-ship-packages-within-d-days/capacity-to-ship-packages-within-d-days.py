def canship(weights,days_have,capacity):
    #find the days needed to ship all the weights under choosen capacity
    days_needed=1
    cweightsum=0
    for w in weights:
        if cweightsum+w<=capacity:
            cweightsum+=w
        else:
            days_needed+=1
            cweightsum=w
        #compare days needed <= days_have (capacity is a valid choice)    
    return days_needed<=days_have            
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        """capacity=max(weights)
        while True:
            if canship(weights,days,capacity):
                break
            else:
                capacity+=1
        return capacity """
        low=max(weights)
        high=sum(weights)
        while low<high:
            mid=(low+high)//2
            if canship(weights,days,mid):
                high=mid
            else:
                low=mid+1
        return low                       

        