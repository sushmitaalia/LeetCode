class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydict = {}
        newlist = []
        for i in strs:
            word = sorted(i)
            word = "".join(word)
            if word not in mydict:
                mydict[word] = []
            mydict[word].append(i)       
        for value in mydict.values():
            newlist.append(value)
        return newlist