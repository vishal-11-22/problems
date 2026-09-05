class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        smallest=prices[0]
        for i in range(1,len(prices)):
            if smallest>prices[i]:
                smallest=prices[i]
            else:
                profit=max(profit,prices[i]-smallest)
        return profit

            