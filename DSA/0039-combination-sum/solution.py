class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def helper(sum_ele,target,arr,start_index):
            if sum_ele==target:
                result.append(arr)
            if sum_ele>target:
                return
            for i in candidates[start_index:]:
                sum_ele+=i
                helper(sum_ele,target,arr+[i],start_index)
                sum_ele-=i
                start_index+=1


        result=[]
        helper(0,target,[],0)
        return result
      


