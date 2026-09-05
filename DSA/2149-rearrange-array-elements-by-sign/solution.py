class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # i=0
        # j=0
        # while j<len(nums):
        #     if nums[j]>0 and i<len(nums):
        #         nums[i],nums[j]=nums[j],nums[i]
        #         i+=2
        #     j+=1
        # return nums
        # pos=0
        # neg=1
        # for i in range(len(nums)):
            
        #     if nums[i]>0 and pos<len(nums):
        #         nums[pos],nums[i]=nums[i],nums[pos]
        #         pos+=2
        #         continue
        #     if nums[i]< 0 and neg<len(nums):
        #         nums[neg],nums[i]=nums[i],nums[neg]
        #         neg+=2
        #         continue
        # return nums
        # pos=[]
        # neg=[]
        # for i in nums:
        #     if i>0:
        #         pos.append(i)
        #     else:
        #         neg.append(i)
        # p,n=0,0
        # for i in range(len(nums)):
        #     if i%2==0:
        #         nums[i]=pos[p]
        #         p+=1
        #     else:
        #         nums[i]=neg[n]
        #         n+=1
        # return nums
        res=[0]*len(nums)
        i=0
        j=1
        for ele in nums:
            if ele>0:
                res[i]=ele
                i+=2
            else:
                res[j]=ele
                j+=2
        return res