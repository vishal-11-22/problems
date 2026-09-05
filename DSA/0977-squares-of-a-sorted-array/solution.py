class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l=[]
        low=0
        high=len(nums)-1
        while(low<=high):
            if nums[low]**2>nums[high]**2:
                l.append(nums[low]**2)
                low+=1
            else:
                l.append(nums[high]**2)
                high-=1
        return l[::-1]

