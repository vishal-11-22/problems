class Solution:
    def calPoints(self, operations: List[str]) -> int:
        st=[]
        for i in operations:
            if i in ['+','D','C']:
                if i=='+':
                    st.append(st[-1]+st[-2])
                if i=='D':
                    st.append(st[-1]*2)
                if i=='C':
                    if st:
                        st.pop(-1)
            else:
                st.append(int(i))
        return sum(st)