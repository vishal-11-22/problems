class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s=0
        for i in nums:
            s+=i
        return (len(nums)*(len(nums)+1)//2)-s