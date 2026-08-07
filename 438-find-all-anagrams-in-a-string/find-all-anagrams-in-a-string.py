class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        #step 1: 
        d2={}
        for i in p:
            d2[i]=d2.get(i,0)+1
        #count the frequencies of characters in substring into d1    
        left=0
        d1={}
        ans=[]
        
        for right in range(len(s)):
            #d1={}
            #ans=[]
            for j in s[right]:
                d1[s[right]]=d1.get(s[right],0)+1  
                if right>=len(p)-1: #checking the validity of window
                    if d1==d2: # comparing hashmaps to check anagrams
                        ans.append(left) #if anagram adding start index to ans
                    # removing the outgoing element- left
                    d1[s[left]]-=1
                    if d1[s[left]]==0:
                        d1.pop(s[left])
                    left+=1
        return ans                
                              
        