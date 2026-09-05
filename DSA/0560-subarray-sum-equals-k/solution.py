class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt=0
        pr_sum=0
        hashmap=dict()
        hashmap[0]=1
        for i,ele in enumerate(nums):
            pr_sum+=ele
            if pr_sum-k in hashmap:
                cnt+=hashmap[pr_sum-k]
            hashmap[pr_sum]=hashmap.get(pr_sum,0)+1
        return cnt