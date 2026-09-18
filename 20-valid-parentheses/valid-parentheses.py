class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        open_b="([{"
        closed_b=")]}"
        st=[]
        for i in s:
            if i in open_b:
                st.append(i)
            else:
                if not st:
                    return False
                else:
                    if i==')' and st[-1]=='(' or st[-1]=='{' and i=='}' or i==']' and st[-1]=='[':
                        st.pop()
                    else:
                        return False 
        return not st                           
        