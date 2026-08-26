class Solution:
    def addBinary(self, a: str, b: str) -> str:
        decimal_a = int(a,2)
        decimal_b = int(b,2)
        addition = decimal_a + decimal_b
        return bin(addition)[2:]        