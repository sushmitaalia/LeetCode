class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxn = 0
        minx = float('inf')
        for i in prices:
            if i < minx:
                minx = i
            profit = i - minx
            if maxn < profit:
                maxn = profit
        return maxn