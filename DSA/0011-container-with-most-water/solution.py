class Solution:
    def maxArea(self, height: List[int]) -> int:
        low=0
        nums=height
        high=len(nums)-1
        max_area=0
        area=0
        while(low<high):
            area=min(nums[high],nums[low])*(high-low)
            max_area=max(max_area,area)
            if nums[low]<nums[high]:
                low+=1
            else:
                high-=1
        return max(area,max_area)
