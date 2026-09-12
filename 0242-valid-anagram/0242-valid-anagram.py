class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        l1 = []
        for i in t:
            l1.append(i)
        for i in s:
            if i not in l1:
                return False
            if i in l1:
                l1.remove(i)
        return True  