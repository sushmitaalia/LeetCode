class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        count = 0
        for i in range(len(t)):
            if count < len(s) and t[i] == s[count]:
                count += 1
        if count == len(s):
            return True
        return False


        # j = 0
        # for i in t:
        #     if j<len(s) and s[j] == i:
        #         j += 1
        # if j == len(s):
        #     return True
        # return False