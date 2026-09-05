class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num=[]
        i=0;j=0
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<nums2[j]:
                num.append(nums1[i])
                i+=1
            else:
                num.append(nums2[j])
                j+=1

        if i<len(nums1):
            while i<len(nums1):
                num.append(nums1[i])
                i+=1
        if j<len(nums2):
            while j<len(nums2):
                num.append(nums2[j])
                j+=1

        if len(num)%2:
            return num[len(num)//2]
        else:
            t1=num[len(num)//2]
            t2=num[(len(num)//2)-1]
            return (t1+t2)/2
