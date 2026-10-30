class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        string1 = {}
        string2 = {}
        value = True
        for c in s:
            if string1.get(c):
                string1[c] = string1.get(c) + 1
            else:
                string1.update({c: 1})
        for c in t:
            if string2.get(c):
                string2[c] = string2.get(c) + 1
            else:
                string2.update({c: 1})
        return string1 == string2
        