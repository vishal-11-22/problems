class Solution:
    def minimumRefill(self, nums: List[int], capacityA: int, capacityB: int) -> int:
        refill_cnt=0
        i=0
        j=len(nums)-1
        a=capacityA
        b=capacityB
        while i<=j:
            if i==j:
                if a>=nums[i] or b>=nums[j]:
                    return refill_cnt
                else:
                    return refill_cnt+1
                    
            if nums[i]<=a:
                a-=nums[i]
                
            else:
                a=capacityA-nums[i]
                refill_cnt+=1
                
            if nums[j]<=b:
                b-=nums[j]
                
            else:
                b=capacityB-nums[j]
                refill_cnt+=1
            i+=1
            j-=1
        return refill_cnt
            