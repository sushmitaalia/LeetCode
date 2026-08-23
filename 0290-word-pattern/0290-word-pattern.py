class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mydict1 = {}
        mydict2 = {}
        new = s.split()
        if len(pattern) != len(new):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in mydict1:
                mydict1[pattern[i]] = new[i]
            if new[i] not in mydict2:
                mydict2[new[i]] = pattern[i]
            if mydict1[pattern[i]] != new[i] or mydict2[new[i]] != pattern[i]:
                return False
        return True