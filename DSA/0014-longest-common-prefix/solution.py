class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)>0:
            a=strs[0]
            for i in range(1,len(strs)):
                out=''
                if len(a)<len(strs[i]):
                    min_len=len(a)
                else:
                    min_len=len(strs[i])
                for j in range(0,min_len):
                    if a[j]==strs[i][j]:
                        out=out+strs[i][j]
                    else:
                        break
                a=out
            return a