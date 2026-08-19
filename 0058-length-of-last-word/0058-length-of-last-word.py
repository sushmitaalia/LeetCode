class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        new = s.split()
        word = new[-1]
        return len(word)

        # new = s.strip()
        # n = len(new)
        # for i in range(-1 , -n-1 , -1):
        #     if new[i] == " ":
        #         return -i -1
        # return n
