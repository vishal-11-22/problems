class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        def prime(n):
            if n==1:
                return False
            for i in range(2,n):
                if n%i==0:
                    return False
            return True
        hash_map=dict()
        for i in nums:
            if i in hash_map:
                hash_map[i]+=1
            else:
                hash_map[i]=1
        for i in hash_map.values():
            if prime(i):
                return True
        else:
            return False