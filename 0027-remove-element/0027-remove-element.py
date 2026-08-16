class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        first , last = 0 , len(nums)-1
        while first <= last:
            if nums[first] == val:
                nums[first] = nums[last]
                last -= 1
            else:
                first += 1
        return first

        # i = 0 
        # last = len(nums) - 1
        # while i <= last:
        #     if nums[i] == val:
        #         nums[i] = nums[last]
        #         last -= 1
        #     else:
        #         i += 1
        # return i
