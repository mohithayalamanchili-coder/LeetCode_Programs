class Solution:
    def calPoints(self, operations: list[str]) -> int:
        st=[]
        for ch in operations:
            if ch!='C' and ch!='D' and ch!='+':
                st.append(int(ch))
            elif ch=='C':
                st.pop()
            elif ch=='D':
                val=st[-1]*2
                st.append(val)
            elif ch=='+':    
                
                st.append(st[-1]+st[-2])
        return sum(st)           
