class Solution:
    def checkDivisibility(self, n: int) -> bool:
        summation = 0
        multiplication = 1
        for i in str(n):
            x = int(i)
            summation += x
            multiplication *= x
        if n % (summation + multiplication) == 0:
            return True
        return False