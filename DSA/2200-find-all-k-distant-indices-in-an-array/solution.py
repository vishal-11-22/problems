class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        i=0;j=0
        res=[]
        while j<len(nums):
            if nums[j]==key:
                while i<len(nums) and abs(i-j)>k:
                    i+=1
                if i>=len(nums):
                    return res
                while i<len(nums) and abs(i-j)<=k:
                    res.append(i)
                    i+=1
            j+=1
        return res
        