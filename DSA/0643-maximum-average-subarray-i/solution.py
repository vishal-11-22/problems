class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
     
        wsum=sum(nums[:k])
        msum=wsum
        j=k
        while(j<len(nums)):
            wsum-=nums[j-k]
            wsum+=nums[j]
            msum=max(wsum,msum)
            j+=1
        return msum/k

