class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        low=0
        high=0
        track=dict()
        tot=0
        max_sum=0
        while(high<len(nums)):
            if nums[high] in track:
                while(nums[high] in track):
                    tot-=nums[low]
                    track.pop(nums[low])
                    low+=1
            tot+=nums[high]
            track[nums[high]]=high
            high+=1
            if high - low > k:
                tot -= nums[low]
                track.pop(nums[low])
                low += 1

            if len(track)==k:
                max_sum=max(max_sum,tot)
                  
           
        return max_sum

                