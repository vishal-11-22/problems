class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans=[]
        left=[]
        right=[]
        ele=1
        for i in range(len(nums)):
            left.append(ele)
            ele=ele*nums[i]
        
        
        ele=1
        for i in range(len(nums)-1,-1,-1):
            right.append(ele)
            ele=ele*nums[i]
        right=right[::-1]
       
        for i in range(len(nums)):
            ans.append(left[i]*right[i])
        

        return ans