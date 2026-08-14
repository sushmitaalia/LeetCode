class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # count = 1
        # i = 0
        # while i < len(nums):
        #     j = i + 1
        #     while j < len(nums):
        #         if nums[i] < nums[j]:
        #             k = j + 1
        #             count += 1
        #             while k < len(nums):
        #                 if nums[j] < nums[k]:
        #                     count += 1
        #                 if count == 3:
        #                     return True
        #                 k += 1
        #         j+=1
        #     i+=1
        # return False. 
        # this works for the given test cases but time complexity is O(N^3) so need to make it more efficient 
        smallest = float('inf')
        middle = float('inf')
        for num in nums:
            if num > middle:
                return True
            if num <= smallest:
                smallest = num
            else:
                middle = num
        return False      