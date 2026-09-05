class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        gt=[]
        lt=[]
        eq=[]
        for i in nums:
            if i>pivot:
                gt.append(i)
            elif i==pivot:
                eq.append(i)
            else:
                lt.append(i)
        return lt+eq+gt