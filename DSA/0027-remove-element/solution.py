class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        low=0
        itr=0
        n=len(nums)
        while(itr<n):
            if nums[itr]!=val:
                nums[itr],nums[low]=nums[low],nums[itr]
                
                low+=1
            itr+=1
        return low