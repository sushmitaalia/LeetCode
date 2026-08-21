class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i , j = 0 , 0
        while j < len(nums):
            if nums[i] == nums[j]:
                j += 1
            else:
                i += 1
                nums[i] = nums[j]
                j += 1
        return i+1
        
        # if len(nums) == 0:
        #     return 0
        # left = 0
        # for right in range(len(nums)):
        #     if nums[left] != nums[right]:
        #         left += 1
        #         nums[left] = nums[right]
        # return left+ 1
        