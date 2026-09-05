class Solution:
    def minLength(self, nums: List[int], k: int) -> int:
        i=0
        j=0
        sum_no=0
        d=dict()
        min_length=float('inf')
        while j<len(nums):
            if nums[j] in d:
                d[nums[j]]+=1
            else:
                sum_no+=nums[j]
                d[nums[j]]=1
                while sum_no>=k:
                    if d[nums[i]]==1:
                        sum_no-=nums[i]
                        d.pop(nums[i])
                    else:
                        d[nums[i]]-=1
                    min_length=min(min_length,j-i+1)
                    i+=1
            j+=1

        return min_length if min_length!=float('inf') else -1


































        # i=0
        # j=0
        # tracker=dict()
        # sum_no=0
        # min_length=float('inf')
        # while j<len(nums):
        #     if nums[j] not in tracker:
        #         tracker[nums[j]]=1
        #         sum_no+=nums[j]
        #         while sum_no>=k:
        #             if sum_no-nums[i]<k:
        #                 min_length=min(min_length,j-i+1)
        #                 break
        #             else:
        #                 if tracker[nums[i]]>0:
        #                 sum_no-=nums[i]
        #                 tracker.pop(nums[i])
        #             i+=1
        #     else:
        #         tracker[nums[j]]+=1            
        #     j+=1
        # return min_length


                