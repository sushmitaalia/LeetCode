class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        l1 = []
        l2 = []
        for i in x:
            l1.append(i)
            l2.append(i)
        l1.reverse()
        if l1 == l2:
            return True
        else:
            return False
