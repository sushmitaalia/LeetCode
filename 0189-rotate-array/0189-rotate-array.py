class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        def reverse(nums,left,right):
            while left < right:
                nums[left] , nums[right] = nums[right] , nums[left]
                left , right = left + 1, right - 1
        reverse(nums , left = 0 , right = len(nums)-1)
        reverse(nums , left = 0 , right = k-1)
        reverse(nums , left = k , right = len(nums)-1)