class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []      
        new = []
        start = nums[0]
        for end in range(len(nums)):
            if end == len(nums) - 1:
                if start == nums[end]:
                    new.append(f"{start}")
                else:
                    new.append(f"{start}->{nums[end]}")
                break
            if nums[end] + 1 != nums[end+1]:
                if start == nums[end]:
                    new.append(f"{start}")
                else:
                    new.append(f"{start}->{nums[end]}")
                start = nums[end+1]
        return new