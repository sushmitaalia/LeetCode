class Solution:
    def isHappy(self, n: int) -> bool:
        store = set()
        while n != 1 and n not in store:
            store.add(n)
            sqr_sum = 0
            for i in str(n):
                sqr_sum += int(i) ** 2
            n = sqr_sum
        if n == 1:
            return True
        return False