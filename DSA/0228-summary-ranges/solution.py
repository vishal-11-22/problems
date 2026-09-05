class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        start=0
        ans=[]
        for j in range(1,len(nums)+1):
            if j==len(nums) or nums[j]!=nums[j-1]+1:
                if start==j-1:
                    ans.append(f'{nums[start]}')
                else:
                    ans.append(f'{nums[start]}->{nums[j-1]}')
                start=j
        return ans
