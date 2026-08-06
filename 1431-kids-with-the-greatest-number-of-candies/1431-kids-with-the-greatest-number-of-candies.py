class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        output = []
        n = max(candies)
        for i in candies:
            if i + extraCandies >= n:
                output.append(True)
            else:
                output.append(False)
        return output