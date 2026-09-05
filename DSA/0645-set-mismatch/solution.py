class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        hashmap=dict()
        res=[]
        sum_val=0
        for i in nums:
            if i in hashmap:
                res.append(i)
            else:
                hashmap[i]=1
                sum_val+=i
        n=len(nums)
        res.append(abs(n*(n+1)//2-sum_val))
        return res