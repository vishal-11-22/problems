class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        ele=nums[0]
        for i in nums[1:]:
            ele=ele^i
        return ele