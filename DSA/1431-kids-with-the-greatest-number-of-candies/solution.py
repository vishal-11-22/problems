class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans=[]
        max_count=max(candies)
        for i in candies:
            if i+extraCandies>=max_count:
                ans.append(True)
            else:
                ans.append(False)
        return ans