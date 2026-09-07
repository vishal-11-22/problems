class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        nums=[i if i==1 else -1 for i in  nums]
        hashmap=dict()
        prefix_sum=[]
        curr_sum=0
        for i in nums:
            curr_sum+=i
            prefix_sum.append(curr_sum)
        max_len=0
        for i in range(len(prefix_sum)):
            if prefix_sum[i]==0:
                max_len=max(max_len,i+1)
            else:
                if prefix_sum[i] in hashmap:
                    max_len=max(max_len,i-hashmap[prefix_sum[i]])
                else:
                    hashmap[prefix_sum[i]]=i
        return max_len