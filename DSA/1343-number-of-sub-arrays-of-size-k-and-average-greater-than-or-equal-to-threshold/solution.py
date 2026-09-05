class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        sum_ele=k*threshold
        wsum=sum(arr[:k])
        j=k
        i=0
        cnt=0
        if wsum>=sum_ele:
            cnt+=1

        while j<len(arr):
           wsum+=arr[j]-arr[j-k]
           if wsum>=sum_ele:
            cnt+=1
           j+=1
        return cnt

