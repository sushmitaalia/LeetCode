class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maximum = float('-inf')
        avg = 0
        context = sum(nums[:k])
        for i in range(0,len(nums)-k+1):
            if i > 0:
                context += nums[i+k-1] - nums[i-1]
            avg = context / k
            if avg > maximum:
                maximum = avg
        return maximum     