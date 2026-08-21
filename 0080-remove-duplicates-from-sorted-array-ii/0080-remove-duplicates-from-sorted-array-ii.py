class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        flag = True
        i , j = 0 , 1
        while j < len(nums):
            if nums[i] == nums[j] and flag == True:
                flag = False
                i += 1
                nums[i] = nums[j]
                j += 1
            elif nums[i] == nums[j] and flag == False:
                j += 1
            else:
                i += 1
                nums[i] = nums[j]
                j += 1
                flag = True
        return i+1      