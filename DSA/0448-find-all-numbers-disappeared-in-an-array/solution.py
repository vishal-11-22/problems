class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[-1]*(n+1)
        for i in nums:
            ans[i]=1
        res=[]
        for i in range(len(ans)):
            if ans[i]==-1 and i!=0:
                res.append(i)
        return res
        