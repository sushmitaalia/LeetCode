class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        l1 = []
        for i in magazine:
            l1.append(i)
        for i in ransomNote:
            if i not in l1:
                return False
            if i in l1:
                l1.remove(i)
        return True
        