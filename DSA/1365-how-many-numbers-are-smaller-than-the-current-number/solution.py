class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        numbers=[0]*101
        for i in nums:
            numbers[i]+=1
        cnt=0
        for i in range(1,len(numbers)):
            numbers[i]+=numbers[i-1]
        ans=[]
        for i in nums:
            if i==0:
                ans.append(0)
            else:
                ans.append(numbers[i-1])
        return ans

        