class Solution:
    def trap(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        lmax=rmax=result=0
        while left<right:
            if height[left]<height[right]:
                if lmax<height[left]:
                    lmax=height[left]
                else:
                    result+=lmax-height[left]
                left+=1

            else:
                if height[right]>rmax:
                    rmax=height[right]
                else:
                    result+=rmax-height[right]
                right-=1
        return result
