class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        
        st = {}
        ts = {}

        for i in range(len(s)):
            if s[i] in st and st[s[i]] != t[i]:
                return False
            elif s[i] not in st and t[i] in ts:
                return False
            else:
                st[s[i]] = t[i]
                ts[t[i]] = s[i]
        return True