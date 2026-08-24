class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        a = set(nums1)
        b = set(nums2)
        new1 = []
        new2 = []
        for num in a:
            if num not in b:
                new1.append(num)
        for num in b:
            if num not in a:
                new2.append(num)
        return [new1 , new2]