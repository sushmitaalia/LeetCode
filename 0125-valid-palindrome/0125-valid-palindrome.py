class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ""
        if len(s) == 0:
            return True
        for i in range(len(s)):
             if 65<=ord(s[i])<=90 or 97<=ord(s[i])<=122 or 48<=ord(s[i])<=57:
                new += s[i].lower()
        i , j = 0 , len(new)-1
        while i < (len(new)) // 2:
            if new[i] != new[j]:
                return False
            i+=1
            j-=1
        return True
        

        # new = ""
        # flag = True
        # for i in range(len(s)):
        #     if  s[i] != " ":
        #         flag = False
        #         break
        # if flag == True:
        #     return True
        # for i in range(len(s)):
        #     if 65<=ord(s[i])<=90 or 97<=ord(s[i])<=122 or 48<=ord(s[i])<=57:
        #         new += s[i].lower()
        # n = len(new)
        # for i in range(n//2):
        #     if new[i] != new[n-i-1]:
        #         return False
        # return True