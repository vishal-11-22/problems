class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d=dict()
        ans=[]
        for i in range(len(nums)):
            if target-nums[i] in d:
                ans.append(d[target-nums[i]])
                ans.append(i)
            else:
                d[nums[i]]=i
        return ans