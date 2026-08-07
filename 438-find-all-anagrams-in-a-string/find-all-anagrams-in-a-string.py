class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        #step 1: 
        d2={}
        for i in p:
            d2[i]=d2.get(i,0)+1
        left=0
        d1={}
        ans=[]
        
        for right in range(len(s)):
            #d1={}
            #ans=[]
           
          
                
            d1[s[right]]=d1.get(s[right],0)+1 
            if right>=len(p)-1:
                if d1==d2:
                    ans.append(left)
                    # removing the outgoing element- left
                d1[s[left]]-=1
                if d1[s[left]]==0:
                    d1.pop(s[left])
                left+=1
        return ans                
                              
        