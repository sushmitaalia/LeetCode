class Solution:
    def countCommas(self, n: int) -> int:
        count = 0
        lower = 1000
        while lower <= n:
            count += (n - lower + 1)
            lower *= 1000
        return count