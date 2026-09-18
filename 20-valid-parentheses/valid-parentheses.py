class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        open_b="([{"
        closed_b=")]}"
        d=dict(zip(closed_b,open_b)) # ')' : '(',']':'[','}':'{'
        st=[]
        for i in s:
            # open brackets go into stack
            if i in open_b:
                st.append(i)
            else:        # when a close bracket is encountered
                if not st:       # if stack is empty , sequence is invalid
                    return False
                else:
                    # check if stack top is corresponding open bracket for this close
                    if d[i]==st[-1]:
                        st.pop()
                    else:
                        return False 
        return not st                           
        