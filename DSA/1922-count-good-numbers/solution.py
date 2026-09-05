class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod=(10**9) + 7
        odd=n//2
        if n%2==0:
            even=odd
        else:
            even=odd+1

            
        return (pow(5,even,mod)*pow(4,odd,mod))%mod