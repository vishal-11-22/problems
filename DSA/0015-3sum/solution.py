class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        s=set()
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            k=len(nums)-1
            while j<k:
                sum_ele=nums[i]+nums[j]+nums[k]
                if sum_ele==0:
                    s.add((nums[i],nums[j],nums[k]))
                    j+=1
                    k-=1
                elif sum_ele>0:
                    k-=1
                else:
                    j+=1
        return list(s)
