class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        total=0
        cnt=0
        for i in range(1,n+1):
            if i in banned:
                continue
            if total+i>maxSum:
                return cnt
            total+=i
            cnt+=1
        return cnt            