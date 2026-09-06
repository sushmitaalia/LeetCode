class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        summation = 0
        minLength = float('inf')
        for right in range(len(nums)):
            summation += nums[right]
            while summation >= target:
                minLength = min(minLength , right-left+1)
                summation -= nums[left]
                left += 1
        if minLength == float('inf'):
            return 0
        return minLength