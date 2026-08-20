class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mydict1 = {}
        mydict2 = {}
        for i in range(len(s)):
            if s[i] not in mydict1:
                mydict1[s[i]] = t[i]
            if t[i] not in mydict2:
                mydict2[t[i]] = s[i]
            if mydict1[s[i]] != t[i] or mydict2[t[i]] != s[i]:
                return False
        return True