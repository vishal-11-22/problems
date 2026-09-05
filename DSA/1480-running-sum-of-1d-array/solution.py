class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        tot=0
        ans=[]
        for i in nums:
            tot+=i
            ans.append(tot)
        return ans
          