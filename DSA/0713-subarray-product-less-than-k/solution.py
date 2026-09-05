class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1:
            return 0
        i=0
        j=0
        product=1
        cnt=0
        while j<len(nums):
            product*=nums[j]
           
            if product>=k:
                while product>=k and i<len(nums):
                    product//=nums[i]
                    i+=1
             
            cnt+=j-i+1
            j+=1
        return cnt