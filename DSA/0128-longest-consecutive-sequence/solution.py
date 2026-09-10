class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len=0
        hash_set=set(nums)
        for i in hash_set:
            if i-1 not in hash_set:
                start=i
                cnt=1
                while start+1 in hash_set:
                    cnt+=1
                    start+=1
                max_len=max(max_len,cnt)
        return max_len 
            