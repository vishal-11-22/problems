class Solution:
    def check(self, nums: List[int]) -> bool:
        is_rotated=False
        is_sorted=True
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                is_sorted=False
                if is_rotated:
                    return False
                else:
                    is_rotated=True
        if nums[-1]>nums[0]:
            is_rotated=False
        # if is_sorted:
        #     return True
        return is_rotated or is_sorted