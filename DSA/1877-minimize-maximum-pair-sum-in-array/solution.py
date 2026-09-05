class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        low=0
        res=0
        high=len(nums)-1
        while(low<high):
            res=max(res,nums[low]+nums[high])
            high-=1
            low+=1
        return res