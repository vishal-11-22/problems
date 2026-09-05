class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        cnt=0
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                if  i and nums[i-1]<nums[i+1]:
                    nums[i]=nums[i+1]
                
                elif i and  nums[i-1]>nums[i+1]:
                    nums[i+1]=nums[i]
                    
                else:
                    nums[i]=nums[i+1]
                cnt+=1
        if cnt>1:
            return False
        return True