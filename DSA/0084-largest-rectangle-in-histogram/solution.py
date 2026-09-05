class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        stack=[]
        max_area=float('-inf')
        nse=[n]*len(heights)
        psm=[-1]*len(heights)
        for i in range(len(heights)-1,-1,-1):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop(-1)
            if stack:
                nse[i]=stack[-1]
            stack.append(i)
        stack=[]
        for i in range(len(heights)):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop(-1)
            if stack:
                psm[i]=stack[-1]
            stack.append(i)
        
        for i in range(len(heights)):
              
            area=(nse[i]-psm[i]-1)*heights[i]
            max_area=max(max_area,area)
        return max_area










        # if len(heights)==1 or len(heights)==2:
        #     return max(heights)
        # low=0
        # high=len(heights)-1
        # max_area=float('-inf')
        # while low<high:
        #     area=min(heights[low],heights[high])*(high-low)
        #     max_area=max(max_area,area)
        #     if low<high:
        #         low+=1
        #     else:
        #         high-=1
        # return max_area