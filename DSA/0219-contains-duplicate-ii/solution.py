class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d=dict()
        for i,j in enumerate(nums):
            if j in d:
                if abs(d[j]-i)<=k:
                    return True
                
                
            d[j]=i
        return False