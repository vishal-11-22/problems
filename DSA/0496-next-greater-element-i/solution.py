class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st=[]
        ng=[-1]*(len(nums2))
        for i in range(len(nums2)-1,-1,-1):
            while st and st[-1]<=nums2[i]:
                st.pop(-1)
            if st:
                ng[i]=st[-1]
            st.append(nums2[i])
        mp=dict()
        for i in range(len(nums2)):
            mp[nums2[i]]=ng[i]
        ans=[]
        for i in nums1:
            ans.append(mp[i])
        return ans
                
