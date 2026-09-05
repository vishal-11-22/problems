class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_cnt=0
        cnt=0
        for i in range(len(nums)):
            if nums[i]==0:
                max_cnt=max(max_cnt,cnt)
                cnt=0
            else:
                cnt+=1
        return max(max_cnt,cnt)