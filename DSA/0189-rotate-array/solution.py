class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        if k == 0: 
            return
        
        t = nums[-k:]
        nums[k:] = nums[:-k]
        nums[:k] = t
        