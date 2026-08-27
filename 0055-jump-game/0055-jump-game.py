class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_index = len(nums)-1
        max_reach = 0
        i = 0
        while i < len(nums):
            if i > max_reach:
                return False            
            if i + nums[i] > max_reach:
                max_reach = i + nums[i]
            if max_reach >= last_index:
                return True
            i += 1  
        return True