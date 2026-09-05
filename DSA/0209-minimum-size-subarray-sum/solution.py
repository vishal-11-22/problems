class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length=float('inf')
        tot=0
        i=0
        low=0
        high=0
        while(high<len(nums)):
            if tot>=target:
                while(tot>=target):
                    min_length=min(min_length,high-low)
                    tot-=nums[low]
                    low+=1
                
            else:
                tot+=nums[high]
                high+=1

        while(tot>=target):
                    min_length=min(min_length,high-low)
                    tot-=nums[low]
                    low+=1
        return 0 if min_length==float('inf') else min_length
