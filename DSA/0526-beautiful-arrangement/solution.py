class Solution:
    def countArrangement(self, n: int) -> int:
        self.res=0
        nums=list(range(n+1))

        def dfs(val):
            if val==0:
                self.res+=1
                return 
            for i in range(val,0,-1):
                nums[i],nums[val]=nums[val],nums[i]

                if nums[val]%val ==0 or val%nums[val]==0:
                    dfs(val-1)

                nums[i],nums[val]=nums[val],nums[i]
        dfs(n)
        return self.res