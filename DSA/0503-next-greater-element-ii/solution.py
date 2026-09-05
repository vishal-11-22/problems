class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        st=[]
        ng=[-1]*(len(nums))
        for i in range(len(nums)-1,-1,-1):
            while st and st[-1]<=nums[i]:
                st.pop(-1)
            st.append(nums[i])

        for i in range(len(nums)-1,-1,-1):
            while st and st[-1]<=nums[i]:
                st.pop(-1)
            if st:
                ng[i]=st[-1]
            st.append(nums[i]) 

        return ng
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # n = len(nums)
        # ans = [-1] * n
        # stack = []
        
        # for i in range(2*n-1,-1,-1):
        #     j = i % n
        #     while stack and stack[-1] <= nums[j]:
        #         stack.pop()
        #     if stack:
        #         ans[j] = stack[-1]
        #     stack.append(nums[j])
        
        # return ans
