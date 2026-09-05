class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        cnt=0
        max_len=0
        i=0;j=0
        while j<len(nums):
            if nums[j]==0:
                cnt+=1
            
            if cnt>k:
                while cnt>k:
                    if nums[i]==0:
                        cnt-=1
                    i+=1
            max_len=max(max_len,j-i+1)
            j+=1
        return max_len
