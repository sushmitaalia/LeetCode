class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        a = len(strs)
        if a == 0 :
            return ""
        strs.sort()
        first = strs[0]
        last = strs[-1]
        n = len(first)
        i = 0
        while i < n and first[i] == last[i]:
            i += 1
        output = ""
        for i in range(i):
            output += first[i]
        return output    