class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt=1
        res=nums[0]
        for i in range(1,len(nums)):
            if nums[i]==res:
                cnt+=1
            else:
                cnt-=1
            if cnt==0:
                res=nums[i]
                cnt=1
        return res