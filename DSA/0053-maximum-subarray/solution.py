class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total=float('-inf')
        curr_sum=0
        for i in nums:
            curr_sum+=i
            total=max(curr_sum,total)
            if curr_sum<0:
                curr_sum=0
        return total