class Solution:
    def isPalindrome(self, s: str) -> bool:
        proc_str=""
        for i in s:
            if i.isalnum():
                proc_str+=i.lower()
        left,right=0,len(proc_str)-1 
        while left<right:
            if proc_str[left]!=proc_str[right]:
                return False
            else:
                left+=1
                right-=1
        return True                   